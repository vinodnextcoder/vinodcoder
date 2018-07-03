import collections
dict1=collections.defaultdict(lambda : 'Key Not found')
dict1['a']=1 
dict1['b']=2 
print  dict1['a']
print "for key not find"
print  dict1['c']
