##### ------------------ Misc bodge stuff

ngrok http 80

echo curl -G http://127.0.0.1:4040/api/tunnels

cd ~/POSTGRAD/Docker/Notflix

cp -r local/videofiles/test data/* local/videofiles/todo_dashify

# DON'T FORGET TO CHANGE THE PURCHASE PAGE ADDRESS!!!
echo "DON'T FORGET TO CHANGE THE PURCHASE PAGE ADDRESS!!!"

##### ------------------ remove existing docker infrastructure

docker stop payment-db logins-db subscription-db \
     login-history login-attempts usage-db \
         pyserving videoserver video-rest mongo-video \
             rec_server rest-login

docker rm payment-db logins-db subscription-db \
     login-history login-attempts usage-db \
         pyserving videoserver video-rest mongo-video \
             rec_server rest-login

docker network rm user video login
docker volume rm $(docker volume ls -qf dangling=true)

##### ------------------ volumes - don't need to run
#docker volume create --name tvshows-data
#docker volume create --name films-data
#docker volume create --name tvshows-conf
#docker volume create --name films-conf
docker volume create --name mongo-conf
docker volume create --name mongo-data
docker volume create --name todo-python
docker volume create --name encoded-video
docker volume create --name login-mysql
docker volume create --name sub-mysql
docker volume create --name pay-mysql
docker volume create --name usage-history
docker volume create --name login-attempts

##### ------------------ networks
docker network create --subnet=172.24.0.0/16 user

##### ------------------ mongo - videos
docker run -dt --name mongo-video -p 28002:27017 \
    --restart=unless-stopped \
    -v mongo-conf:/data/db \
    -v mongo-data:/home \
        mongo

#docker run -it --rm --link mongo-video:mongo mongo mongo mongo/video_db

##### ------------------ restheart - video
docker run -d -p 90:8080 --name video-rest \
    --restart=unless-stopped \
    --link mongo-video:mongodb \
        softinstigate/restheart

##### ------------------ video encoding dashify
docker run -it --rm --name dashit \
    -v $PWD/local/videofiles/todo_dashify/:/todo_dashify \
    -v todo-python:/todo_python \
        dashifying:3 \
        /bin/bash -c \
        'python /usr/bin/group-dash.py'

##### ------------------ video encoding dataget
docker run -it --rm --name dataget \
    --link video-rest:rest \
    -v todo-python:/todo_python \
    -v encoded-video:/encoded_video \
    data-get:alp3 \
        /bin/ash -c \
        'python /py_scripts/process_video_files.py'

##### ------------------ neo4j
docker run -d --name rec_server \
    --restart=unless-stopped \
    -p 7474:7474 -p 7687:7687 \
        neo4j

##### ------------------ populate neo4j
docker run -it --rm --name neo-add \
    --restart=unless-stopped \
    --link video-rest:rest \
    --link rec_server:neorec\
        neo-data-get:alp1 \
        /bin/ash -c 'python /py_scripts/neo4j_data.py'

##### ------------------ videoserver
docker run  -dt --name videoserver -p 81:80 \
    --restart=unless-stopped \
    -v encoded-video:/data \
         videoserver

##### ------------------ python webserver
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

##### ------------------ MYSQL - logins    -e MYSQL_RANDOM_ROOT_PASSWORD \
docker run -itd --name logins-db \
    --net user \
    --restart=unless-stopped \
    -v login-mysql:/var/lib/mysql \
    -e MYSQL_ROOT_PASSWORD=3298hfk4jgiet3r \
    -e MYSQL_DATABASE=logins_db \
        dijksterhuis/mysql-login:prod

##### ------------------ MYSQL - subscription
docker run -itd --name subscription-db \
    --net user \
    --restart=unless-stopped \
    -v sub-mysql:/var/lib/mysql \
    -e MYSQL_ROOT_PASSWORD=3598ybnw49f4hf \
    -e MYSQL_DATABASE=subscription_db \
        dijksterhuis/mysql-subs:prod

##### ------------------ MYSQL - payments
docker run -itd --name payment-db \
    --net user \
    --restart=unless-stopped \
    -v pay-mysql:/var/lib/mysql \
    -e MYSQL_ROOT_PASSWORD=sdgkjb349hvnwie \
    -e MYSQL_DATABASE=payment_db \
        dijksterhuis/mysql-payment:prod

#docker run -it --link payment-db:mysql  --rm mysql sh -c \
#    'exec mysql -h"$MYSQL_PORT_3306_TCP_ADDR" -P"$MYSQL_PORT_3306_TCP_PORT" -uroot -p'


##### ------------------ mysql rest API (WIP)
#docker run -it --name rest-mysql --restart=unless-stopped \
#    -v $PWD/repo/pymyrest-login/py_scripts/:/app:ro \
#    rest-login:0.1 /bin/bash

#docker network connect --ip 172.24.0.7 user rest-mysql

##### ------------------ REDIS USER VIEWS DB
docker run -d --name usage-db \
    --restart=unless-stopped \
    --net user \
     -v usage-history:/data \
         redis:alpine

##### ------------------ REDIS LOGIN ATTEMPTS DB
docker run -d --name login-attempts \
    --restart=unless-stopped \
    --net user \
    -v login-attempts:/data \
        redis:alpine

##### ------------------ REDIS SUCCESSFUL LOGIN HISTORY
docker run -d --name login-history \
    --restart=unless-stopped \
    --net user \
    -v login-history:/data \
        redis:alpine
