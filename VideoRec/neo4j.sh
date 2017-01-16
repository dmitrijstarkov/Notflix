docker stop rec_server
docker rm rec_server

docker run -d --name rec_server \
    -p 7474:7474 -p 7687:7687 \
        neo4j