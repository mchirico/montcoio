FROM golang:1.13.7-alpine3.11



ADD . $GOPATH/src/servercorsslpv

RUN apk	update && apk add git

RUN go install servercorsslpv

#
#
FROM alpine:latest
RUN mkdir -p /etc/certs
COPY fullchain.pem /etc/certs/fullchain.pem
COPY key.pem /etc/certs/key.pem
RUN apk	update && apk add ca-certificates && rm -rf /var/cache/apk/*



COPY --from=0 /go/bin/servercorsslpv .
ENV PORT 8080
CMD ["./servercorsslpv"]

# To run this
#  docker build -t us.gcr.io/mchirico/servercorsslpv:latest .

#  docker push us.gcr.io/mchirico/servercorsslpv:latest

# kubectl run hello-server --image us.gcr.io/mchirico/gosslserver:latest --port 8080
# kubectl delete service hello-server

# // Not working ..
# kubectl rolling-update myapp --image=us.gcr.io/mchirico/hello:latest --image-pull-policy Always


