n = int(input(""))

people = []
#available = []
for i in range(n):
    people.append(list(input("")))

#print(people, n)

'''
temp = []
for i in range(len(people)):
    temp = []
    for j in range(5):
        if people[i][j] == 'Y':
            temp.append(j + 1)
    
    available.append(temp)
'''
#print(people)

days = {}
availablepeople = 0
for i in range(n):# for every day
    availablepeople = 0
    for j in range(4):# check if every participant is available
            if people[i][j] == 'Y':
                availablepeople += 1
    days[n] = availablepeople
    # Loop through the people and see which day has the most available people

days_sorted = sorted(days, reverse=True)
#print(days, days_sorted)

for l in range(len(days_sorted)):
    print(days_sorted[l] + 1, end='')
    if l == len(days_sorted):
        print(',', end='')