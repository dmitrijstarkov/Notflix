## Notflix

Video Streaming service using DevOps infrastructure and methodology.

To run in one go, run the global shell scripts file. You must use ngrok use the payments service (requires editing loopback url) or have it depolyed on an azure machine (payapl don't allow sandbox loopbacks to localhost unfortunately). 

You must have set up a local directory - local/videofiles/todo_dashify
This is where the test video files must be stored before runtime

Individual shells scripts are provided for individual container running.

There are test video files that will be used for Demo.

Tech used:

* docker networking
* docker links
* redis
* mongodb
* restheart API
* mysql
* docker builds
* docker persistant volumes
* Python - Flask webserver
* nginx video server
* bootstrap
* Jinja templates

probably some more too...

List of containers:

* Dashifying - Encodes video files and moves between volumes on completion
* Data-get uses OMDBapi.com's api to get video meta data, and store for streaming. 
* Mongo-video - stores video meta data
* Restheart API - handles webseerver requests to mongo-video
* neo4j-data-get - reads data in the mongo-video db, reformats it and stores it in neo4j for recommendations.
 * n.b. this is storing the data incorrectly, didn't have time to fix
* rec_server - stores movie realtionships via genre, writers, directors, actors (for recommendation generation)
* logins-db - stores login data for users - only allows stored procedures to be run by the webserver - no general SELECT statements.
* payments-db - stores payments from paypal
* subscriptions-db - stores subscription details from paypal
* usage-db - stores a user's viewing history
* login-attempts-db - restricts user access after 5 login attemots in 60 seconds
* login history db - stores datetime of user logins

Things I wanted to do but didn't have time:

* Docker swarm - without sorting replication out for all database, this would have been difficult. Understand it and have seperate code for set-up that I could demo.
* mysql rest api - have all the mysql requests code. combining with python flask would allow for this to be developed into a *secure* REST docker container.
