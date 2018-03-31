import pymongo
from pymongo import MongoClient
client = MongoClient('localhost:27017')
db = client.testvinod
emp1=raw_input("enter rollno")
emp2=raw_input("enter name")
emp3=raw_input("enter city")
emp4=raw_input("enter course")
db.stud.insert_one(
{
"id":emp1,
"name":emp2,
"city":emp3,
"course":emp4
})

print "data insert to db"
