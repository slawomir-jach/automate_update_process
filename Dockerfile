FROM centos

RUN yum install -y epel-release which curl bash zip unzip   gcc musl-dev g++ libxml2 
RUN yum repolist
RUN yum install -y python36 python36-setuptools python-pip python36-dev python36-devel

RUN  curl -s "https://get.sdkman.io" | bash
RUN source "$HOME/.sdkman/bin/sdkman-init.sh"
RUN mkdir -p /automate/info_files/
COPY  info_files/current_version.json /automate/info_files/
COPY  main.py /automate/
COPY  request_info.py /automate/ 
RUN  mkdir -p /usr/local/lib/python3.6/site-packages/
RUN easy_install-3.6 pip
RUN pip3 install  --upgrade pip
RUN pip3 install  requests && pip3 install  justext \
&& pip3 install  pandas  
