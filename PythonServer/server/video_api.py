# ------------------------------- #
# Global constants for REST calls #
# ------------------------------- #

__author__ = 'mturatti'

_BASE_URL = "http://172.17.0.3:8080"
_DATABASE = '/video_db'
VIDEO_DATABASE_URL = _BASE_URL + _DATABASE
VIDEO_COLLECTION_URL = VIDEO_DATABASE_URL + "/video_cat"

VIDEO_HEADERS = {'Content-type': 'application/hal+json', 'Accept': '*/*'}