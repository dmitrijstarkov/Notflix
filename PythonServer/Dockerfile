# Webserver running python files
# Server files mapped as volume on run
# map to /home/server

FROM tiangolo/uwsgi-nginx-flask:latest
MAINTAINER dijksterhuis "mrobeson@dundee.ac.uk"
RUN apt-get update
RUN apt-get --upgrade install -y tar git curl nano wget dialog net-tools python-pip python-dev build-essential python-distribute
RUN pip install --upgrade pip virtualenv flask requests
EXPOSE 5000
EXPOSE 90
RUN rm /app/*
RUN cd /app