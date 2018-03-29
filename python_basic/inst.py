List=[4,5,1,3,9]
for j in range(1,len(List)):

    key=List[j]
    i=j-1
    print List[i],key
    while i>=0 and List[i]>key:
        
        List[i+1]=List[i]
        i=i-1
    List[i+1]=key
#print List
