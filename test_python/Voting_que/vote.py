#author vinod khetade
#email vinodk275@gmail.com
import time
import re
f=open("input_vote.txt","r")
r=f.read()
f.close()
r=r.replace("\r","")
r=r.strip()
dict_vot={}
data=r.split("\n")
dele=[]
dict_count={}
vot_name=[]
del_name=[]
seen = set()
c=0
flag=0
# split input for voting
for x in data:
    my=re.split("(delegate|pick)",x)
    if my[2] in my and my[0] in my and "pick" in my:
        dict_count[my[2]]=c
        dele.append(my[0])
        flag=1
        
        if my[2] not in seen:
            dict_vot[my[2]]=my[0]
            vot_name.append(my[0])
            del_name.append(my[2])
        
#counter for vote Count
counter = dict()
for dd in dict_vot:
    if not dd in counter:
        counter[dd] = 1
    else:
        counter[dd] += 1

if flag==1:
    for x in data:
        my=re.split("(delegate|pick)",x)
        if my[2] in my and my[0] in my and 'delegate' in my:
            for d in dele:
                for dd in dict_vot:
                    if dict_vot[dd]==d:
                        counter[dd] += 1
                    else:
                        #print ""
                        counter[dd] = 1
        
            

print "**********Voting Count****************"
for vc in counter:
    print vc,counter[vc]


