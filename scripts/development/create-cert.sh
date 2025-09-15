#!/bin/bash
set -e

MINIKUBE_IP="localhost"

CERT_DIR="./certs"
mkdir -p $CERT_DIR

ECOSYSTEM_NS="ecosystem"
ECOSYSTEM_SECRET="tls-ecosystem"
openssl genrsa -out $CERT_DIR/ecosystem.key 2048
openssl req -x509 -nodes -days 365 \
  -key $CERT_DIR/ecosystem.key \
  -out $CERT_DIR/ecosystem.crt \
  -subj "/CN=code-roaster.ai" \
  -addext "subjectAltName=DNS:code-roaster.ai"
kubectl create namespace $ECOSYSTEM_NS --dry-run=client -o yaml | kubectl apply -f -
kubectl delete secret $ECOSYSTEM_SECRET -n $ECOSYSTEM_NS --ignore-not-found
kubectl create secret tls $ECOSYSTEM_SECRET \
  --cert=$CERT_DIR/ecosystem.crt \
  --key=$CERT_DIR/ecosystem.key \
  -n $ECOSYSTEM_NS

MON_NS="monitoring"
MON_SECRET="tls-monitoring"
openssl genrsa -out $CERT_DIR/monitoring.key 2048
openssl req -x509 -nodes -days 365 \
  -key $CERT_DIR/monitoring.key \
  -out $CERT_DIR/monitoring.crt \
  -subj "/CN=monitoring.code-roaster.ai" \
  -addext "subjectAltName=DNS:monitoring.code-roaster.ai"
kubectl create namespace $MON_NS --dry-run=client -o yaml | kubectl apply -f -
kubectl delete secret $MON_SECRET -n $MON_NS --ignore-not-found
kubectl create secret tls $MON_SECRET \
  --cert=$CERT_DIR/monitoring.crt \
  --key=$CERT_DIR/monitoring.key \
  -n $MON_NS

HOSTS_ENTRIES=(
    "code-roaster.ai"
    "monitoring.code-roaster.ai"
)
for DOMAIN in "${HOSTS_ENTRIES[@]}"; do
    if ! grep -q "$DOMAIN" /etc/hosts; then
        echo "$MINIKUBE_IP $DOMAIN" | sudo tee -a /etc/hosts
    fi
done

echo "[INFO] TLS secrets created and /etc/hosts is up to date."