from content import Content

__author__ = 'carlos'

from bottle import get, post, request, run  # or route
import json
import content

@post('content/')
def create():
    content = Content.from_json(request.json['cmd'])
    return "OK"

run(host='localhost', port=8080, debug=True)
