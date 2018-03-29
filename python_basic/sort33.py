List=[2,1,4,5,2,6,6]
List.sort()
print List
n=len(List)
for i in range(0,n-1,2):
    List[i],List[i+1]=List[i+1],List[i]
print "new List"
print List
