number = int(input())
numbercopy = number
i = 2
ans = ""
long = 0
while number != 1:
    if number % i == 0:
        number = number // i
        ans = ans + str(i) + "*"
    if number % i != 0:
        i += 1
if numbercopy == 1:
    print(number, "=", "1")
else:
    ans = ans[:-1]
    print(numbercopy, "=", ans)
