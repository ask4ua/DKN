pods_check(){
	while true
	do
		echo ""
	    echo "Pods:"
		kubectl get pods
		echo ""
		echo "Logs:"
		kubectl logs webapp | tail -n 5
		echo ""
		echo "Events:"
		kubectl describe pod webapp | tail -n 5
		
		if kubectl get pod/webapp | grep -i running >> /dev/null
		then
			break
		fi
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
		if curl -X GET 10.5.11.203:320${NUM} >> /dev/null 2>&1
		then
			curl -X GET 10.5.11.203:320${NUM}
			sleep 5
			break
		else
			pods_check
		fi
		sleep 1
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
	pods_check
    curl_check 
	sleep 10
done
