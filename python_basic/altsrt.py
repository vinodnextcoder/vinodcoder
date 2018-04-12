List=[3,1,6,6,8,6,0]
print "Originl List\n"
print List
n=len(List)
List.sort()

i=0
j=n-1
while(i<j):
    print List[j],
    j-=1
    print List[i],
    i+=1
if (n%2!=0):
    print List[i],


