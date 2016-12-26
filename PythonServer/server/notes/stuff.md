stuff to install: python

requests
flask
flask-request
restheart?

### NOTES


##### MySQL

docker run --name logindb -e MYSQL_ROOT_PASSWORD=admin -p 3306:3306 -d mysql

docker run -it --link logindb:mysql --name int_mysql_ --rm mysql sh -c 'exec mysql -h"$MYSQL_PORT_3306_TCP_ADDR" -P"$MYSQL_PORT_3306_TCP_PORT" -uroot -p"$MYSQL_ENV_MYSQL_ROOT_PASSWORD"'

