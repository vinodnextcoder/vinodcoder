t = int(input())
for i in range(t):
    suvojit = 0
    suvo = 0
    s = input()
    suvojit = s.count("SUVOJIT")
    suvo = s.count("SUVO")
    print('SUVO = ',suvo-suvojit,', SUVOJIT = ',suvojit,sep='')
