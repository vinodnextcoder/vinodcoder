ACS=256
def getcount(str1):
    count=[0]*ACS
    print count
    max=-1
    c=-1
    for i in str1:
        count[ord(i)]+=1;
        print ord(i)
    for i in str1:
        if max < count[ord(i)]:
            max=count[ord(i)]
            c=i

    return c
str1="vinodiivinod"
print getcount(str1)
