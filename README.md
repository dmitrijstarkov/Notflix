## Notflix 0.0.10

### Python:

#### Module Requirements:

* **Flask** (http://flask.pocoo.org/) to do the web serving.
* **Requests** (https://pypi.python.org/pypi/requests) to do the the API requests.
* **JSON** (https://pypi.python.org/pypi/json) to format things as JSON strings
* **FUNCTOOLS** (https://pypi.python.org/pypi/functools) to use wrap()

#### How it works

* @app.route(website page , http request methods) - defines "web pages"
* def page() - functions to run when page's app.route is called by client
* def loginrequired() - controls which pages need logins to work
* rendertemplate - display template (templates folder)
  * note that templates work differently to base html
  * there is one base template (nav menu, footers etc.)
  * other templates are then called inside that base template, generating the actual page
* redirect(url_for()) - move to a different page for whatever reason
* GETS from a webpage with Flask need to be made with input forms

#### More how it works

		payloadtv=get_resource(EP_COLLECTION_URL,params=None).json()

-- assign to payload tv the result of GET call to mongo db collection "episodes" with no parameters (bring back all the data)

    app = Flask(__name__)

-- defines the script as "app"

    if __name__ == '__main__':
        app.run(host='0.0.0.0',debug=True,port=82)

-- where to host the server (dokcer container maps local:80 to python:82)

### Getting video data from Mongo container

* Lines 55 - 81 in the main.py file
* Does two GET calls (not finised films yet), convert the JSON to dictionary, passes dictionary to webpage.
* Once client clicks on a button (input form submit in catalogue.html), POSTs back to the server, video page retrieved and streamed


### Video Server Container

* Uses Nginx (jgmp VideoServer container)
* Videos stored in hashed folders with video files + metadata.txt (imdb id)
* manifest.mpd is the file needed to play the stream with dash.js
* Python connects to VideoServer container through localhost:81/hashed folder/manifest.mpd
* UPDATE: I have an extra service to add. Takes the imdb id and calls from OMDBapi.com, then adds to the video catalogue database.

