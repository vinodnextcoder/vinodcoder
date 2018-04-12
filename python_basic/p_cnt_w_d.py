string=raw_input("Enter String:")
count1=0
count2=0
for i in string:
      if(i.isdigit()):
            count1=count1+1
      count2=count2+1
print("Number of digits is:")
print(count1)
print("Number of characters is:")
print(count2)
