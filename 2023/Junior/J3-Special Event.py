num_people = int(input(""))

d = dict()

for i in range(1, 5+1):
    d[i] = 0

for _ in range(num_people):
    schedule = input()

    for i in range(5):
        if schedule[i] =='Y':
            d[i + 1] += 1
        
max_value = max(d.values())

result = []

for key, value  in d.items():
    if value == max_value:
        result.append(key)

for i in range(len(result)):
    print(result[i], end="")

    if i != len(result) - 1:
        print(",", end="")
    else:
        print("")
