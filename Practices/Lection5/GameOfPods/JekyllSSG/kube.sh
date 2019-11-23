#!/bin/bash
kubectl config set-credentials drogo --client-certificate=/root/drogo.crt --client-key=/root/drogo.key
kubectl config set-context developer --cluster=kubernetes --user=drogo --namespace=kubernetes