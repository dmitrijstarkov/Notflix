## MUST DO

#### pyserver

* turn off server debugging
* pyserving port 80
* copy py files on build

#### Other dbs

* split mongo videos - film + tv + series - FUCKING PORTS OR SOMETHING ?!?!?!?
* change / SET UP new admin passwords ?!?!

#### CI + Docker

* finalise Dockerfiles for builds
  * mysql have done! - define specific version of mysql to use?
  
* JENKINS?!?!?

* Docker swarm (not the databases)

#### Done

* Design page for recent payments
* When was last payment made? - subs wrapper
  * currently a string in db, needs to be date
  * change session values for subs check
* paypal check the data is being written!
* dataget - change file moves
* check the user set ups for mysql
* Admin password - randomise?
* set up users that CAN ONLY use SPs
* NAV LINKS
  * Dictionary
  * Make dependant on session values (if logged in, then only login/register)  
* ERROR MESSAGES  
  * dictionary too  
  
#### IF I HAVE TIME

* extra subscription / payment data into the databases?
  * then could use name etc.

* Subscription to Inactive? have a "cancel subscription" option?  

* mysql rest api
  * ALL queries through to it
  * then off to different databases from there

* PURCHASE PAGE
  * the ngrok static domain needs to be setup
  * ENV variables?
  * sign up and have a static domain?
  * would be solved by an azure jenkins build - static IP

* NETWORKS - connections via container names!
  * easier to do services + swarm mode then
    * login network? - redises
    * usage - redis + neo4j ???
    * users (mysql)

    * (webserver - pyserving, restheart?)
    * (videos - dataget, mongo, rest)
  * will need to rebuild some images - connection names will change

* flask mail

* Neo4j - recommendations
 * user history - from the redis store?
 * user recommendation page?
   * use carousel - py script input
   * can use redis to store "SCORED SETS"

* docker swarm mode

* logs files from all the python scripts?

#### DBs

* TIMESTAMPS ?!?!
* NEO 4J!
* Admin passwords ALL need to change

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
* when film watched, add a relationship

* HOW TO DO THE WALKS for the reccomendations?



## Not bothering with


* clean up the episodes page
  * ordering
  * what if no image

* Welcome page? - site logo?

* redis - what else can I use this for? so easy to set up!!
  * write usage db to mysql on session close? or mongo?
  * user film ratings?