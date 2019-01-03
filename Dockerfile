FROM alpine

ENV HTTP_PROXY="http://172.17.0.1:3128"
RUN apk add curl bash zip unzip python3 
RUN  curl -s "https://get.sdkman.io" | bash
CMD [ "mkdir /automate"]
COPY info_files/* /automate
COPY main.py /automate
COPY request.py /automate 
RUN  python3 /automate/main.py
