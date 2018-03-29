List=[3,4,1,8,2,2]
print "Original List"
print List
n=len(List)-1
i=0
while i<n:
    print List[i],List[n],"=",List[n],List[i]
    List[i],List[n]=List[n],List[i]
    i+=1
    n-=1
print "Reverse List"
print List
