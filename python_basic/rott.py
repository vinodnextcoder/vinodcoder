List=[2,1,3,4]
n=len(List)
for i in range(2):
    temp=List[n-1]
    for j in range(n-1,0,-1):
        List[j]=List[j-1]
    List[0]=temp

print List
