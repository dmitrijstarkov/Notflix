docker stop usage-db
docker rm usage-db

docker run -d --name usage-db \
    --restart=unless-stopped \
    --net user \
     -v usage-history:/data \
         redis:alpine