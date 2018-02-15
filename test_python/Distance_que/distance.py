# author vinod khetade
#vinodk2757@gmail.com
import math
list1 = ["LEFT","WALK","WALK","RIGHT","WALK"]
c = 0
x1 = 0
y1 = 0
for x in list1:
	if x == "LEFT":
		c = 1
	if c ==1 and x == "WALK":
		x1 = x1 + 1
	if x == "RIGHT":
		c =2
	if c ==2 and x=="WALK":
		y1 = y1 + 1
x = math.pow(x1 , 2)
y = math.pow(y1, 2)
z = math.sqrt(x+y)
z = round(z,2)
print "**************Distance Output******************"
print z
