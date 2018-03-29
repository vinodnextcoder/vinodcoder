import pprint
n=50
d=dict()
for i in range(1,n+1):
    d[i]=i*i
pp = pprint.PrettyPrinter(depth=6)
pp.pprint (d)

for i in range(1,n+1):
    if(n%i==0):
        print i
