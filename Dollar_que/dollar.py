import time
import re
f=open("input_doll.txt","r")
r=f.read()
f.close()
r=r.replace("\r","")
r=r.strip()
data=r.split("\n")
penny = 1
nickel = 10
dime = 5
quarter = 25
doll=0
q = 0
d = 0
n = 0
p = 0
# reading file input manipulates dllars
for value in data:
    value= float(value)
    intpart,decimalpart = int(value),value-int(value)
    deci=str(decimalpart).split(".")
    if len(deci)==1:
        doll=int(deci[0])
    if len(deci)==2: 
        doll=intpart
        i=int(deci[1])
        if i>=25:
            q = i/quarter
            i %= quarter
        if i>=10:
            n = i/nickel
            i %= nickel
        if i>=5:
            d = i/dime
            i%=dime
        if i>0:
            p = i/penny
            i = 0

    print "******************Dollars OutPut***************"
    print doll,"Dollars"
    print q,"quarters"
    print n,"nickel"
    print p,"Penny"
    print "******************END******************"


