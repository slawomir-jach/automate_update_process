FROM centos

RUN yum install -y epel-release which curl bash zip unzip python36  gcc musl-dev g++ libxml2 python36-setuptools
RUN  curl -s "https://get.sdkman.io" | bash
RUN source "$HOME/.sdkman/bin/sdkman-init.sh"
RUN mkdir -p /automate/info_files/
COPY . /info_files/current_version.json /automate/info_files/
COPY . main.py /automate/
COPY . request_info.py /automate/ 
RUN yum install -y python36 && yum install -y python34-setuptools && mkdir -p /usr/local/lib/python3.6/site-packages/
RUN easy_install-3.6 pip
RUN pip36 install  --upgrade pip
RUN pip36 install  requests && pip36 install --proxy="http://172.17.0.1:3128" justext \
&& pip36 install  pandas  
