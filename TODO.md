## Docker

* Networking? - set up restheart on a network, connect webserver to network
* Makes it isolated
* A usage DB container? With REST API?
* Volumes
  * Video db volume
  * mongodb config??!


## DBs

* TIMESTAMP EVERRRRRRRRYYYYTHING

#### Users

* STILL NEED user DB! - Hold the fb data?

#### Graph - recommendations

* This needs to run on:
  * webserver (users watches film)
  * new data load from videoprep
  
* Neo4j model v0.0.1:
  * User watched - Node
  * Film - Node
    * Director
    * Actor
    * Genre
    * Weightings on the edges for "watched"
      * number of times watched etc.
      * higher weigthing for genres already watched
  * if watched film x - these films might be good to watch

## Services

#### Videofiles/VideoPrep

* Run on the a seperate docker container?
  * Volume link to videos folder
  * Directory hash and mongo put - run through Cron?

* Run in videoprep?
  * stop dashify when running
  * cron update rules?
  * DO:
    * hold webservice? - or run replica update?
    * run hashing, update mongodb - can i get replication going?
    * start dashifying script
    * if dashifying at 12 am (etc.)
      * stop dashify.sh
      * move unprocessed files!!!

#### Users

* Logins db + auth
  * facebook? https://blog.miguelgrinberg.com/post/oauth-authentication-with-flask
  * db https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-v-user-logins
  * db2 (vid) https://www.youtube.com/watch?v=_vrAjAHhUsA

* Registration
  * fb?
  * db?

* Account settings

* Payment
  * paypal? https://developer.paypal.com/docs/classic/payflow/gs_ppa_hosted_pages/

* py video file put mongodb documents - mongodb_data.py
  * needs to run as a part of videoprep
    * run dashify on todo
    * copy metadate file
    * run mongodb_data.py - with put?
    
* TV + Season / Film directories on webpage?


## Webserver

* Use docker ENV variables to set the Video API IP to the one in /etc/hosts of container (restpy linked container)
* Mongo DB IP needed by both the webserver and the mongo db put script