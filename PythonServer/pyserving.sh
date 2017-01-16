docker stop pyserving
docker rm pyserving

docker run -dt --name pyserving --restart=unless-stopped -p 80:82 \
    --link videoserver:vidstream \
    --link video-rest:restpy \
    --link rec_server:rec_server \
        dijksterhuis/pyserver:7 \
        /bin/bash

docker network connect --ip 172.24.0.7 user pyserving

#-v $PWD/repo/PythonServer/server:/app:ro \
#docker exec -it pyserving /bin/bash -c 'python main.py'

docker exec -d pyserving /bin/bash -c 'python main.py'