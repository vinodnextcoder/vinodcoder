#!/usr/bin/env python 
import collections
freq_dict={}
alphabet = "abcdefghijklmnopqrstuvwxyz"
c=0
for l in alphabet:
    freq_dict[l]=c
    c+=1
count1=[]
testCases = int(input())
for i in range(testCases):
    string = raw_input()
   
    cnt=0
    for let in string:
        for key,value in freq_dict.items():
            if key==let:
                cnt+=int(value)
    count1.append(cnt)



