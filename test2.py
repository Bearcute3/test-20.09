a = int(input())
b = int(input())
n = 0
n1 = 0
a1 = ""
b1 = ""
while a > 0:
    a1 = str(a % 2) + a1
    a = a // 2
while b > 0:
    b1 = str(b % 2) + b1
    b = b // 2
a1 = int(a1)
b1 = int(b1)
while b1 > 0 and a1 > 0:
    if a1 % 2 != b1 % 2:
        n += 1
        a1 = a1 // 10
        b1 = b1 // 10
    else:
        a1 = a1 // 10
        b1 = b1 // 10
if a1 > 0:
    while a1 > 0:
        a1 = a1 // 10
        n1 = n1 + 1
if b1 > 0:
    while b1 > 0:
        b1 = b1 // 10
        n1 = n1 + 1
print(n1 + n)
