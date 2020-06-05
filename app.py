import falcon
import json
from falcon import API
from db.util.db_pool import MySQLPool

from api.v1.user import UserCollection
from api.v1.userV1 import UserCollectionV1

import os

api = falcon.API()
dbhost = os.getenv('DBHOST')
dbport = os.getenv('DBPORT')
dbuser = os.getenv('DBUSER') 
dbpassword = os.getenv('DBPASSWORD') 
dbname = os.getenv('DBNAME') 
dbpool = os.getenv('DBPOOL') 

dbconfig = {
    "host":dbhost,
    "port":dbport,
    "user":dbuser,
    "password":dbpassword,
    "database":dbname,
	"pool_size":dbpool
}

mysqlpool = MySQLPool(**dbconfig)
api.add_route('/v0/users',UserCollection(mysqlpool))
api.add_route('/users',UserCollectionV1(mysqlpool))