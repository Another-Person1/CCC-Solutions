n = int(input(""))
peppers = []
for i in range(n):
    peppers.append(input(""))

shu = 0

for j in range(len(peppers)):
    if peppers[j] == "Poblano":
        shu += 1500
    elif peppers[j] == "Mirasol":
        shu += 6000
    elif peppers[j] == "Serrano":
        shu += 15500
    elif peppers[j] == "Cayenne":
        shu += 40000
    elif peppers[j] == "Thai":
        shu += 75000
    elif peppers[j] == "Habanero":
        shu += 125000

print(shu)