# ------------------------------- #
# Global constants for REST calls #
# ------------------------------- #

_BASE_URL = "http://localhost:90" # CHANGEIT
_DATABASE = '/videos'
VIDEO_DB_URL = _BASE_URL + _DATABASE
VIDEO_COLLECTION_URL = VIDEO_DB_URL + "/video_cat"
SERIES_NFO_COLLECTION_URL = VIDEO_DB_URL + "/video_cat"

VIDEO_HEADERS = {'Content-type': 'application/hal+json', 'Accept': '*/*'}