## Notflix

Video Streaming service using DevOps infrastructure and methodology.

Docker containers used for microservices, Jenkins used for Continuous Deployment.

You must have set up a local directory - local/videofiles/todo_dashify
This is where the test video files must be stored before runtime

Individual shells scripts are provided for individual container running.

There are test video files that will be used for Demo.

Software and databases used:

* docker networking
* docker links
* redis
* mongodb
* restheart API
* mysql
* docker builds
* docker persistant volumes
* Python - Flask
* nginx video server
* bootstrap

Docker containers:

* Dashifying - Encodes video files and moves between volumes on completion
* Data-get uses OMDBapi.com's api to get video meta data, and store for streaming. 
* Mongo-video - stores video meta data
* Restheart API - handles webseerver requests to mongo-video
* neo4j-data-get - reads data in the mongo-video db, reformats it and stores it in neo4j for recommendations.
 * n.b. not happy with how the data is stored, didn't have time to fix
* rec_server - stores movie realtionships via genre, writers, directors, actors (for recommendation generation)
* logins-db - stores login data for users - only allows stored procedures to be run by the webserver - no general SELECT statements.
* payments-db - stores payments from paypal
* subscriptions-db - stores subscription details from paypal
* usage-db - stores a user's viewing history
* login-attempts-db - restricts user access after 5 login attemots in 60 seconds
* login history db - stores datetime of user logins

Things I wanted to do but didn't have time:

* Docker swarm - replication out for MySQL containers was difficult.
* mysql rest api - have all the mysql requests code. combining with python flask would allow for this to be developed into a *secure* REST docker container.
* 
