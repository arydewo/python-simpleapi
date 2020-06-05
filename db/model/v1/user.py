import mysql.connector as myconnector

class User(object):
    def __init__(self, mysqlpool):
       	super().__init__()
        self.mysqlpool = mysqlpool
    
    def queryUsers(self):
        mysqlpool = self.mysqlpool
        sql = "SELECT id, first_name, last_name FROM users LIMIT 5 OFFSET 0"
        result = mysqlpool.execute(sql,isMode="select")
        return result
