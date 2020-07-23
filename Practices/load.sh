#!/bin/bash
pods_check(){
	kubectl get pods
	kubectl logs webapp | tail -n 5
	kubectl describe pod webapp | tail -n 5

	while true
	do
		if kubectl get pod/webapp | grep -i running > /dev/null
		then
			break
		fi
		pods_check
		sleep 1
	done

}

pods_delete(){
	kubectl delete pod webapp
	kubectl delete pod db
}

curl_check(){
	while true
	do
	 	echo "another try to get http from webapp"
		if `curl -X GET 10.5.11.203:320${NUM}`
		then
			curl -X GET 10.5.11.203:320${NUM}
			sleep 5
			break
		else
			pods_check
			sleep 1
		fi
		RETRY_CYCLES = $(expr $RETRY_CYCLES - 1)
        done	
}

NUM=${USER:7:2}
echo "NUM=$NUM"
echo "Replacing port 32000 to 320$NUM"
find ./ -name "*.y*ml" -exec sed -i -e "s/32000/320$NUM/g" {} \;

while true
do
	kubectl delete namespace $USER
	kubectl create namespace $USER
	kubectl get pods -A
	kubectl get namespaces
	kubectl apply -f Section4/pod/webapp_pod.yaml
	kubectl apply -f Section4/pod/db_pod.yaml
	kubectl apply -f Section4/configmap/webapp_configmap.yaml
	kubectl apply -f Section4/service/webapp_service.yaml
	kubectl apply -f Section4/service/db_service.yaml
	kubectl apply -f Section4/service/webappdb_service.yaml
	kubectl apply -f Section4/service/webapp_service.yaml
	kubectl apply -f Section4/secret/webapp_secret.yaml
	pods_check
	pods_delete

	kubectl apply -f Section4/pod/webapp_pod_configmap_secret_init.yaml
	kubectl apply -f Section4/pod/db_pod_secret_volume.yaml
    pods_checl
    curl_check 
	sleep 10
done
