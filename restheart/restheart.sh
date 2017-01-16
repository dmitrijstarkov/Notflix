docker stop video-rest
docker rm video-rest

docker run -d -p 90:8080 --name video-rest \
    --link mongo-video:mongodb \
        softinstigate/restheart