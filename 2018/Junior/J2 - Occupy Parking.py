n = int(input(""))
yesterday = [*input("")]
today = [*input("")]

occupied = 0
for i in range(n):
    if today[i] == yesterday[i] and today[i] == 'C' and yesterday[i] == 'C':
        occupied += 1

print(occupied)
