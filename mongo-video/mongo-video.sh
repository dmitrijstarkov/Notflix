docker run -dt --name mongo-video -p 28002:27017 \
    -v mongo-conf:/data/db \
    -v mongo-data:/home \
        mongo