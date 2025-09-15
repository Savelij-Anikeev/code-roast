#!/bin/bash
set -e

sudo -v

echo "[PERMISSIONS] sudo permissions given."

echo "[INFO] Building Docker images for Minikube..."

eval $(minikube docker-env)
docker build -t frontend -f ./apps/frontend/Dockerfile.development ./apps/frontend
docker build -t auth-service -f ./apps/auth.service/Dockerfile.development ./apps/auth.service
docker build -t reviews-service -f ./apps/reviews.service/Dockerfile.development ./apps/reviews.service
docker build -t rest-gateway-service -f ./apps/rest-gateway.service/Dockerfile.development ./apps/rest-gateway.service
docker build -t ws-gateway-service -f ./apps/ws-gateway.service/Dockerfile.development ./apps/ws-gateway.service
eval $(minikube docker-env -u)

echo "[INFO] Enabling namespaces"
kubectl apply -f k8s/development/services/namespace.yaml
kubectl apply -f k8s/development/monitoring/namespace.yaml

echo "[INFO] Applying manifests..."
kubectl apply -f k8s/development/statefuls/ -R
kubectl apply -f k8s/development/services/ -R
kubectl apply -f k8s/development/monitoring/ -R

echo "[INFO] Enabling ingress..."
minikube addons enable ingress

kubectl apply -f k8s/development/ingresses/ -R

echo "[INFO] Setting up proxy..."
minikube tunnel &

echo "[INFO] Done."