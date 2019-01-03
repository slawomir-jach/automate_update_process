FROM alpine

ENV HTTP_PROXY="http://172.17.0.1:3128"
RUN apk add curl bash zip unzip 
RUN  curl -s "https://get.sdkman.io" | bash
COPY