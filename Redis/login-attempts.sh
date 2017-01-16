docker stop login-attempts
docker rm login-attempts

docker run -d --name login-attempts \
    --restart=unless-stopped \
    --net user \
    -v login-attempts:/data \
        redis:alpine