number = input("")
list = []
list.append(number)
lastDir = ""
while int(number) != 99999:
    number = input("")
    if int(number) == 99999:
        break
    list.append(number)

for i in list:
    sumOf = int(i[0]) + int(i[1])
    digits3 = i[2] + i[3] + i[4]
    if i == "99999":
        break
    if sumOf % 2 == 1:
        print("left", digits3)
        lastDir = "left"
    elif sumOf % 2 == 0 and sumOf !=0:
        print("right", digits3)
        lastDir = "right"
    elif sumOf == 0:
        print(lastDir, digits3)
