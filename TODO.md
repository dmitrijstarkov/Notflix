## Docker

* Networking? - set up restheart on a network, connect webserver to network
* Makes it isolated

## Services

* OMDB API - http://www.omdbapi.com/
 * Use the IMDB ID for video_encode and metadata.txt?
 * Then when python wants catalogue data, OMDB call based on ID
 * DEF GETs:
   * Type (movie/film)/ Poster / Genre / Plot / Duration / Year / Rated / Title
* Maybe GETs:
   * Awards / Actors/ Director / Writer / Metascore / imdbRating
   
   http://www.omdbapi.com/?i=tt0082971&plot=short&r=json

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
  * got it to write to json videofile directory
  * can i get it to do a put/post db?
  * needs to run as a part of videoprep
    * run dashify on todo
    * copy metadate file
    * run mongodb_data.py - with put?
    
* TV + Season / Film directories?

## DBs

* PostgreSQL - Login db?

## Webserver

* Use docker ENV variables to set the Video API IP to the one in /etc/hosts of container (restpy linked container)