# ------------------------------- #
# Global constants for REST calls #
# ------------------------------- #

_BASE_URL = "http://172.17.0.3:8080" # THIS CAN CHANGE!!!
_DATABASE = '/videos'
VIDEO_DATABASE_URL = _BASE_URL + _DATABASE
EP_COLLECTION_URL = VIDEO_DATABASE_URL + "/episode"
FILM_COLLECTION_URL = VIDEO_DATABASE_URL + "/movie"

VIDEO_HEADERS = {'Content-type': 'application/hal+json', 'Accept': '*/*'}