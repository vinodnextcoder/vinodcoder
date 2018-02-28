import re
n=input()
c=0
for i in range(0,n):
    
    input_string=raw_input()
    if re.search("[0-9]{2}",input_string):
        print "Date"
        break
       
