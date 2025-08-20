 cd infrastructure/k8s/


echo -n 'benny' | openssl base64
echo -n '1234' | openssl base64
echo -n 'enemy_soldiers' | openssl base64


oc apply -f mongo-secret.yaml
oc apply -f mongo-pvc.yaml
oc apply -f mongo-deployment.yaml
oc apply -f mongo-service.yaml


