docker stop login-history
docker rm login-history

docker run -d --name login-history \
    --restart=unless-stopped \
    --net user \
    -v login-history:/data \
        redis:alpine