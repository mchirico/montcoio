FROM nginx
RUN mkdir -p /website/s.montcopa.io/html
RUN mkdir -p /etc/letsencrypt/live/s.montcopa.io
RUN mkdir -p /etc/nginx/sites-enabled/
COPY default /etc/nginx/sites-enabled/default
COPY proxy_params /etc/nginx/proxy_params
COPY index.html /website/s.montcopa.io/html/index.html
COPY fullchain.pem /etc/letsencrypt/live/s.montcopa.io/fullchain.pem
COPY privkey.pem /etc/letsencrypt/live/s.montcopa.io/privkey.pem
COPY nginx.conf /etc/nginx/nginx.conf
COPY dhparam.pem /etc/ssl/certs/dhparam.pem

# To run this ...
# docker build -t us.gcr.io/mchirico/nginxpig:latest .
# docker push us.gcr.io/mchirico/nginxpig:latest



#  docker push us.gcr.io/mchirico/nginxs:latest

# kubectl run hello-server --image us.gcr.io/mchirico/hellos:latest --port 8080

# kubectl expose deployment hello-server --type LoadBalancer --port 443 --target-port 8080 
# 

# Local IPs only work with service
# kubectl apply -f hello-service.yaml
# kubectl get service




# kubectl delete service hello-server
# kubectl delete deployment hello-server

# // Not working ..
# kubectl rolling-update myapp --image=us.gcr.io/mchirico/hello:latest --image-pull-policy Always


