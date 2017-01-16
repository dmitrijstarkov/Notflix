docker run -it --rm --name neo-add \
    --link video-rest:rest \
    --link rec_server:neorec\
        neo-data-get:alp1 \
        /bin/ash -c 'python /py_scripts/neo4j_data.py'