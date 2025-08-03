#!/bin/bash
set -e

sudo echo "[PERMISSIONS] sudo permissions given."

echo "[INFO] Building Docker images for Minikube..."
eval $(minikube docker-env)
docker build -t backend:dev ./apps/backend -f ./apps/backend/Dockerfile.development
docker build -t frontend:dev ./apps/frontend -f ./apps/frontend/Dockerfile.development

echo "[INFO] Enabling ingress..."
minikube addons enable ingress

echo "[INFO] Applying manifests..."
kubectl apply -f k8s/development/configMaps/
kubectl apply -f k8s/development/statefulsets/
kubectl apply -f k8s/development/deployments/
kubectl apply -f k8s/development/services/
kubectl apply -f k8s/development/secrets/
kubectl apply -f k8s/development/ingresses/

echo "[INFO] Setting up proxy..."
minikube tunnel

echo "[INFO] Done."