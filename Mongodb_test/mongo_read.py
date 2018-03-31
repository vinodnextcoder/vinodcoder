from pymongo import MongoClient
client = MongoClient('localhost:27017')
db = client.testvinod
try:
    student = db.stud.find()
    print '\n All student \n'
    for s in student:
        print s

except Exception, e:
    print str(e)
