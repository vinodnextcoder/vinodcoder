#!/usr/bin/env python                                                                                                                          
n =input()
Vowel_list=['A', 'E','I','O',"U",'a','e', 'i', 'o', 'u']
for i in range(0,n):
    count=0
    input_string=raw_input()
    for s in input_string:
        if s inVowel_list:
            count+=1
            
    print count
