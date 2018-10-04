import re
f=open("rfe.txt","r")
r=f.read()
f.close()
data=r.split("\n")
for x in data:
    if re.search('([0-9]{1,2}\s+[a-zA-Z ]+[.]{2,}\s?[0-9]\s?[-]?[0-9]?)',x,re.IGNORECASE):
        match=re.search('([0-9]{1,2}\s+[a-zA-Z ]+[.]{2,}\s?[0-9]\s?[-]?[0-9]?)',x,re.IGNORECASE).group()
        print match
        

    elif re.search('([0-9]{1,2}\s+([a-zA-Z ]+[0-9]-?[0-9]?))',x,re.IGNORECASE):
        match=re.search('([0-9]{1,2}\s+([a-zA-Z ]+[0-9]-?[0-9]?))',x,re.IGNORECASE).group()
        print match
    break

    # if re.search('([0-9]{1,2}\s+([a-zA-Z ]+[0-9]-?[0-9]?))|([0-9]\s+[a-zA-Z ]+[.]{2,}\s?[0-9]\s?[-]?[0-9]?)',x,re.IGNORECASE):
    #     match=re.search('([0-9]{1,2}\s+([a-zA-Z ]+[0-9]-?[0-9]?))|([0-9]\s+[a-zA-Z ]+[.]{2,}\s?[0-9]\s?[-]?[0-9]?)',x,re.IGNORECASE).group()
    #     print match
