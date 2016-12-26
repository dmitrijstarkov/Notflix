# Video prep build
# map volume to /encoded_video when running
# check out min distros?
# New dashify scripts 

FROM ubuntu:16.04
MAINTAINER dijksterhuis "mrobeson@dundee.ac.uk"
RUN apt-get update
RUN apt-get install -y ffmpeg gpac nano
RUN mkdir -p /encoded_video
RUN mkdir -p /encoded_video/todo
COPY dashify2.sh /usr/bin/dashify.sh
RUN chmod a+x /usr/bin/dashify.sh
RUN cd /encoded_video