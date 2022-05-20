class fileModule:
    def __init__(self):
        self.path = "/var/log/app.log"

    def checkIfExists(self):
        """file system prepare """
        argsFile = open(self.path, "a+")
        argsFile.close()
       
    def insertPostData(self, user, time):
        """inserting given data """
        argsFile = open(self.path, "a+")
        argsFile.write(user+": "+time+"\n")
        argsFile.close()
        return "Success"

    def insertGetData(self):
        """inserting just counter data """
        argsFile = open(self.path, "a+")
        argsFile.write("get\n")
        argsFile.close()
        return "Success"

    def getMetrics(self):
        """metrics harvester """
        file = open(self.path)
        dirtyString = file.read()
        file.close()
        getCounter = postCounter = 0
        for row in dirtyString.split('\n'):
            if row == "get":
                getCounter = getCounter + 1
            elif len(row) > 5 :
                postCounter = postCounter + 1
        return getCounter, postCounter