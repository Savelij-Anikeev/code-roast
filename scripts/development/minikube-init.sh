#!/bin/bash
set -e

echo "[INFO] Starting minikube with Docker driver..."
minikube start --driver=docker --cpus=4 --memory=4096 --addons=metrics-server

echo "[INFO] Installing HAProxy ingress controller..."
kubectl apply -f https://raw.githubusercontent.com/haproxytech/kubernetes-ingress/master/deploy/haproxy-ingress.yaml

echo "[INFO] Minikube IP:"
minikube ip