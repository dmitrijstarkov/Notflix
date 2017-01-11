# Video prep build
# map volume to /encoded_video when running
# check out min distros?
# New dashify scripts 

FROM ubuntu:16.04
MAINTAINER dijksterhuis "mrobeson@dundee.ac.uk"
RUN apt-get update
RUN apt-get install -y ffmpeg gpac nano python
RUN mkdir -p /todo_dashify
RUN mkdir -p /todo_python
COPY dashify.sh /usr/bin/dashify.sh
COPY group-dash.py /usr/bin/group-dash.py
RUN chmod a+x /usr/bin/dashify.sh
RUN chmod a+x /usr/bin/group-dash.py
RUN cd /todo_dashify