docker stop subscription-db
docker rm subscription-db


docker run -itd --name subscription-db \
    --net user \
    --restart=unless-stopped \
    -v sub-mysql:/var/lib/mysql \
    -e MYSQL_ROOT_PASSWORD=3598ybnw49f4hf \
    -e MYSQL_DATABASE=subscription_db \
        dijksterhuis/mysql-subs:prod
