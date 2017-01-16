docker stop videoserver
docker rm videoserver

docker run  -dt --name videoserver -p 81:80 \
    -v encoded-video:/data \
         videoserver