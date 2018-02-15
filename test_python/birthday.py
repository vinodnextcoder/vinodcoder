# author vinod khetade
#email:vinodk2757@gmail.com

import time
import calendar
import re
f=open("input_birthday.txt","r")
r=f.read()
f.close()
r=r.replace("\r","")
r=r.strip()
data=r.split("\n")

# week created static for month 4th
dict_bdate={}
for month in range(04,05):
    c = calendar.monthcalendar(2018, month)
    first_week = c[0]
    second_week = c[1]
    third_week = c[2]
    fourth_week = c[3]
    fifth_week=c[4]
date=[]
# split dates
for x in data:
    name=re.split(" ",x)
    dict_bdate[name[0]]=name[1]
    bdate=re.split("-",name[0])
    date.append(int(bdate[2]))
#cheikng weeks and bday date
weekindex = []
for i in range(0,len(c)):
	for d in date:
		if d in c[i]:
                    weekindex.append(i)
                    break

#Manipulating party date
party_bdate={}
for key in dict_bdate:
    d=re.split("-",key)
    dd=int(d[2])
    mm=int(d[1])
    if mm==month:
        if dd in c[0] and first_week[calendar.SUNDAY]:
            pd=first_week[calendar.SUNDAY]
            bd=d[0]+"-"+d[1]+"-"+str(pd)
            party_bdate[bd]=dict_bdate[key]
        elif dd in c[1] and second_week[calendar.SATURDAY]:
            pd=second_week[calendar.SATURDAY]
            bd=d[0]+"-"+d[1]+"-"+str(pd)
            party_bdate[bd]=dict_bdate[key]
        elif dd in c[2] and third_week[calendar.SATURDAY]:
            pd=third_week[calendar.SATURDAY]
            bd=d[0]+"-"+d[1]+"-"+str(pd)
            party_bdate[bd]=dict_bdate[key]
        elif dd in c[3] and fourth_week[calendar.SATURDAY]:
            pd=fourth_week[calendar.SATURDAY]
            bd=d[0]+"-"+d[1]+"-"+str(pd)
            party_bdate[bd]=dict_bdate[key]
        elif dd in c[4] and fifth_week[calendar.SATURDAY]:
            pd=fifth_week[calendar.SATURDAY]
            #print dd,pd
            bd=d[0]+"-"+d[1]+"-"+str(pd)
            party_bdate[bd]=dict_bdate[key]
print "************Birthday Party Dates************"
for day in party_bdate:
    print day,party_bdate[day]


print "___________________________________________"
