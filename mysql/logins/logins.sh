docker stop logins-db
docker rm logins-db

docker run -itd --name logins-db \
    --net user \
    --restart=unless-stopped \
    -v login-mysql:/var/lib/mysql \
    -e MYSQL_ROOT_PASSWORD=3298hfk4jgiet3r \
    -e MYSQL_DATABASE=logins_db \
        dijksterhuis/mysql-login:prod