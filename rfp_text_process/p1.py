import re
f=open("output.html","r")
r=f.read()
f.close()
data=r.split("\n")
for x in data:
    print x
