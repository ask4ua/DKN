#!/bin/bash
while true
do
	NUM=${USER:7:2}
	echo "NUM=$NUM"
	git stash
	git pull
	find ./ -name "*.y*ml" -exec sed -i -e "s/32000/320$NUM/g" {} \;
	sleep 10
	kubectl create namespace $USER
	kubectl get pods -A
	kubectl get namespaces
	kubectl apply -f Section4/pod/webapp_pod.yaml
	kubectl apply -f Section4/pod/db_podyaml
	kubectl apply -f Section4/configmap/webapp_configmap.yaml
	kubectl apply -f Section4/service/webapp_service.yaml
	kubectl apply -f Section4/service/db_service.yaml
	kubectl apply -f Section4/service/webappdb_service.yaml
	kubectl apply -f Section4/service/webapp_service.yaml
	kubectl apply -f Section4/secret/webapp_secret.yaml
	kubectl get pods
	kubectl logs webapp
	kubectl describe pod webapp
	sleep 10
	kubectl delete pod webapp
	kubectl delete pod db
	kubectl apply -f Section4/pod/webapp_pod_configmap_secret_init.yaml
	kubectl apply -f Section4/pod/db_pod_secret_volume.yaml
	RETRY_CYCLES=100
	SLEEP_TIMER=1
	while [ $RETRY_CYLES > 0 ]
	do
	 	echo "another try to get http from webapp"
		if `curl -X GET 10.5.11.203:320${NUM}`
		then
			break
		else
			kubectl get pods
			kubectl logs webapp
			kubectl describe pod webapp
			sleep $SLEEP_TIMER
		fi
		RETRY_CYCLES = $(expr $RETRY_CYCLES - 1)
        done	       
done
