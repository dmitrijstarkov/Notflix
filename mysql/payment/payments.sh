docker stop payment-db
docker rm payment-db

docker run -itd --name payment-db \
    --net user \
    --restart=unless-stopped \
    -v pay-mysql:/var/lib/mysql \
    -e MYSQL_ROOT_PASSWORD=sdgkjb349hvnwie \
    -e MYSQL_DATABASE=payment_db \
        dijksterhuis/mysql-payment:prod