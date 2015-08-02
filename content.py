from logilab.common import clcommands

__author__ = 'carlos'

import uuid
import json


class Format:
	HTML = 0
	MD = 1
	RST = 2
	SRC = 3
	IMG = 4
	GIST = 5

class ContentData:


    def __init__(self, id, title):
        self.id = id
        self.title = title
        self.authors = set()


class ContentPart:
    def __init__(self, info, format, data):
        self.info = info
        self.format = format
        self.data = data

class Content:

    def __init__(self, content_data):
        self.content_data = content_data
        self.content_parts = []

    @classmethod
    def from_json(cls, json_input):
        return json.loads(json_input, cls=Content)


class CmdResponse:

    def __init__(self, path, level,  msg):
        self.path = path
        self.level = level
        self.msg = msg

"""
message UpdatePart{
	ContentPart part = 1;
	uint32 position = 2;
}

service ContentCmdHandler {
	rpc save (Content) returns (CmdResponse){}
	rpc remove (common.Uuid) returns (CmdResponse){}
	rpc removePart (common.Uuid) returns (CmdResponse){}
	rpc updatePart (UpdatePart) returns (CmdResponse){}
}

"""
