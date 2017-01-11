## MUST DO

* change / !!SET UP!! admin passwords!

* Welcome page? - site logo?

* Account page!!

* redis - what else can I use this for? so easy to set up!!
  * write usage db to mysql on session close? or mongo?
  * 
  
* mysql - subscription table!!
  * session subscriptions check (dependant on mysql)
  * CHANGE THE SESSSION VALUES!!

* finalise Dockerfiles for builds

* JENKINS!

* paypal check!
  * does payment work?
  * can I put the data to mysql?
  * should I have a seperate db ?


## NICE TO HAVE

* mysql - user details??
  * Paypal login?
  
* film ratings??

* Neo4j - recommendations
 * user history - from the redis store?
 * user recommendation page?
   * use carousel - py script input
   * can use redis to store "SCORED SETS"

* docker networks

* docker swarm mode

* logs files from all the python scripts?

______________

### Docker

* Networking? - set up restheart on a network, connect webserver to network
  * Makes it isolated
  * SET IP ADDRESSES TO BE STATIC
* Payapl transaction details 

### DBs

* TIMESTAMPS
* NEO 4J!
* Admin passwords ALL need to change

### Services

#### Graph - recommendations

* This needs to run based on from:
  * webserver (users watches film)
  * new data load from videoprep
  
* Neo4j model v0.0.1:
  * Users Node
  * Film Nodes
    * Director
    * Actor
    * Genre
    * Weightings on the edges for "watched"
      * number of times watched etc.
      * higher weigthing for genres already watched
  * if watched film x - these films might be good to watch

* when films added, add a film node - videoprep
* when user registers in, add a user node - pyserving

#### Videofiles/VideoPrep

* Run in videoprep?
  * stop dashify when running
  * cron update rules?
  * DO:
    * iterate through ONLY todo folder (need to add this)
    * start dashifying script for each new folder
    * run hashing, update mongodb
    * mongo script only puts NEW dox from todo, so nothing gets overwritten

#### Users

* e-mail confirmations? Flask-Mail?
  
* Registration
  * send to purchase page
  * if not completed purchase, drop from database

* Account settings - password change, email change

* Payment
  * paypal? https://developer.paypal.com/docs/classic/payflow/gs_ppa_hosted_pages/

#### Webserver

* Use docker ENV variables to set the Video API IP to the one in /etc/hosts of container (restpy linked container)
* Mongo DB IP needed by both the webserver and the mongo db put script