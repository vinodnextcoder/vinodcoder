import json,re
f=open("2.json","r")
r=f.read()
f.close()
r=r.replace("{","")
r=r.replace("}","")
r=r.replace('"','')
r=r.replace(',','\n')
data=r.split("\n")
List=[]
for x in data:
    n=""
    if "to" in x:
        x=re.sub(r"to\s\s:\s","",x)
        x=x.strip()
        List.append(x)
        #x=re.sub(r"\s","",x)

        # n=x
        # n=re.sub(r'to : ','',n)
        # n=x.strip()
        # List.append(n)
print List
f=open("1.json","r")
r=f.read()
f.close()
r=r.replace("{","")
#r=r.replace("}","")
r=r.replace('"','')
r=r.replace('},','\n')
data=r.split("\n")

for x in data:
    x=x.replace(',','\n')
    data1=x.split("\n")
    idd=""
    for x in data1:
        if "id" in x:
            idd=x
            idd=re.sub(r'id :','',idd)
            idd=idd.strip()
    
    name1=''
    for x in data1:
        if "name" in x:
            name1=x
            name1=re.sub(r'name:','',name1)
            name1=name1.strip()
    idd=""
    for x in data1:
        if "id" in x:
            idd=x
            idd=re.sub(r'id :','',idd)
            idd=idd.strip()
    c=0
    for j in List:
        if idd==j :
            c+=1
    print c,idd,name1
