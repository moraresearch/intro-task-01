import sqlite3

class sqlModule:
    def __init__(self):
        self.con = sqlite3.connect('/var/log/app.sqlite', check_same_thread=False)
        
    def checkIfExists(self):
        """database prepare """
        self.con.execute('create table IF NOT EXISTS users(name CHAR(50),time CHAR(50));')
        self.con.execute('create table IF NOT EXISTS getusers(name CHAR(50),time CHAR(50));')
        self.con.commit()

    def insertPostData(self, user, time):
        """inserting given data """
        dataList = [user, time]
        self.con.execute('insert into users(name, time) values (?,?)', dataList)
        self.con.commit()
        return "Success"

    def insertGetData(self):
        """inserting just counter data """
        dataList = ["get", "get"]
        self.con.execute('insert into getusers(name, time) values (?,?)', dataList)
        self.con.commit()
        return "Success"

    def getMetrics(self):
        """metrics harvester """
        postCounter = self.con.execute('SELECT count(name) FROM users ').fetchone()
        getCounter = self.con.execute('SELECT count(name) FROM getusers ').fetchone()
        return getCounter[0], postCounter[0]