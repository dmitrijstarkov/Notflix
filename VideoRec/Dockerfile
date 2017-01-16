# Webserver running python files
# Server files mapped as volume on run
# map to /home/server

FROM alpine
MAINTAINER dijksterhuis "mrobeson@dundee.ac.uk"
RUN apk update
RUN apk add python nmap curl nano
RUN apk add py-pip
RUN pip install --upgrade pip requests py2neo
RUN mkdir -p /py_scripts
COPY py_scripts/* /py_scripts/
RUN cd /py_scripts
