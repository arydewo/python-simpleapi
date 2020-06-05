import falcon
from db.model.v1.user import User as mdlUser
from collections import OrderedDict
import math
import random
import base64
import logging

class UserController(object):
    def __init__(self, mysqlpool):
       	super().__init__()
       	self.mysqlpool = mysqlpool

    def set_default(obj):
        if isinstance(obj, set):
            return list(obj)
        raise TypeError    

    def queryUsers(self):
        mysqlpool=self.mysqlpool
        User = mdlUser(mysqlpool)
        objOut = type('', (), {})()
        objOut.code = 200
        objOut.desc = "OK"
        tmpResult = None
        tmpResultType = None
        tmpResult = User.queryUsers()
        tmpResultType = tmpResult.__class__.__name__
        
        if "Error" in tmpResultType:
            objOut.code = 500
            objOut.desc = str(tmpResult).replace('\'', '')
        else:
            if tmpResult:
                objOut.data = tmpResult
            else:
                objOut.code = 404
                objOut.desc = "Not Found"
        
        return objOut        
        