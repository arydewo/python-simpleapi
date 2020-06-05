import falcon
import json
from urllib.parse import quote_plus as urlquote, urlparse
from collections import OrderedDict
from ctl.v1.user import UserController as ctlUser

class UserCollection(object):
    def __init__(self, mysqlpool):
       	super().__init__()
       	self.mysqlpool = mysqlpool

    def set_default(obj):
        if isinstance(obj, set):
            return list(obj)
        raise TypeError

    def on_get(self, req, resp, usrId=None):
        reqPath = urlparse(req.url).path
        mysqlpool = self.mysqlpool
        cliUser = ctlUser(mysqlpool)
        result = type('', (), {})()
        result.code = 200
        result.desc = "OK"
        objIn = type('', (), {})()
        objIn.params = req.params;
        objIn.path = urlparse(req.url).path
        result = cliUser.queryUsers()
        if result.code == 200:
            resp.status = falcon.HTTP_200
        elif result.code == 400:
            resp.status = falcon.HTTP_400
        elif result.code == 404:
            resp.status = falcon.HTTP_404
        elif result.code == 500:
            resp.status = falcon.HTTP_500       
        resp.body = json.dumps(result.__dict__,default=str)