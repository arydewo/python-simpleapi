import falcon
import json
from urllib.parse import quote_plus as urlquote, urlparse
from collections import OrderedDict
from db.model.v1.user import User as mdlUser


class UserCollectionV1(object):
    def __init__(self, mysqlpool):
       	super().__init__()
       	self.mysqlpool = mysqlpool

    def set_default(obj):
        if isinstance(obj, set):
            return list(obj)
        raise TypeError

    def on_get(self, req, resp, usrId=None):
        mysqlpool = self.mysqlpool
        User = mdlUser(mysqlpool)
        result = type('', (), {})()
        result.code = 200
        result.desc = "OK"
        tmpResult = None
        tmpResult = User.queryUsers()
        result.data = tmpResult
        resp.status = falcon.HTTP_200
        resp.body = json.dumps(result.__dict__,default=str)