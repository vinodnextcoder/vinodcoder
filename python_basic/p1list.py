def reverse(string):
    if len(string) == 0:
        return string
    else:
        print string[1:]
        return reverse(string[1:]) + string[0]
a = "vinodbhau"
print(reverse(a))
print a[1:]
