FROM alpine
MAINTAINER dijksterhuis "mrobeson@dundee.ac.uk"
RUN apk update
RUN apk add python nmap curl nano
RUN apk add py-pip
RUN pip install --upgrade pip requests
RUN mkdir -p /todo_python
RUN mkdir -p /encoded_video
RUN mkdir -p /py_scripts
COPY py_scripts/ /py_scripts/
RUN cd /
