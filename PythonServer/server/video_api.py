# ------------------------------- #
# Global constants for REST calls #
# ------------------------------- #

_BASE_URL = "http://video-rest:8080" # THIS CAN CHANGE!!!
_DATABASE = '/videos'
VIDEO_DATABASE_URL = _BASE_URL + _DATABASE
TV = VIDEO_DATABASE_URL + "/episode"
MOVIE = VIDEO_DATABASE_URL + "/movie"
SERIES_TRANS = VIDEO_DATABASE_URL + "/series_transform"
SERIES_NAME = VIDEO_DATABASE_URL + "/series_name"


VIDEO_HEADERS = {'Content-type': 'application/hal+json', 'Accept': '*/*'}