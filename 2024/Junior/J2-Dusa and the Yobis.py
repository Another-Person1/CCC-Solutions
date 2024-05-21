d = int(input(""))
yobis = []

while True:
    cinput = int(input(""))
    if cinput < d:
        d = d + cinput
    else:
        print(d)
        break
