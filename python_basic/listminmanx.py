List=[3,2,4,5,6,90]
List.sort()
print List
yes=True
for i in range(1,len(List)):
    
    if (List[i]-List[i-1])>1:
        print List[i],List[i-1]
        yes=False
if yes:
    print True
else:
    print False
