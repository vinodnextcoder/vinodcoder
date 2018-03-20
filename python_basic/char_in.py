string = input()
alphabet = list(map(chr, range(97, 123)))
if set(alphabet) == set(string):
    print('YES')
else:
    print('NO')
