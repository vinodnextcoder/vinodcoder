a=[]
n= int(input("Enter the number of elemnt"))
for x in range(0,n):
    element=int(input( str(x+1)))
    a.append(element)
b = set()
List = []
for x in a:
    if x not in b:
        List.append(x)
        b.add(x)

print List
