# Webserver running python files
# Server files mapped as volume on run
# map to /home/server

FROM tiangolo/uwsgi-nginx-flask
MAINTAINER dijksterhuis "mrobeson@dundee.ac.uk"
RUN apt-get update
RUN apt-get --upgrade install -y nmap curl nano dialog net-tools python-pip python-dev build-essential python-distribute
RUN pip install --upgrade pip virtualenv flask requests flask-mysql flask_sqlalchemy redis MySQL-python py2neo
RUN rm /app/*
COPY server/ /app/
RUN cd /app
EXPOSE 80