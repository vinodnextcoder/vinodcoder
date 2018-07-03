def splitarr(List,n,k):
    for i in range(0,k):
        x=List[0]
        #print i,x
        for j in range(0,n-1):
            print List[j],List[j+1]
            List[j]=List[j+1]
        List[n-1]=x

List=[2,3,1,3,4,5,11]
n=len(List)
pos=2
splitarr(List,n,pos)

