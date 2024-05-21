n = int(input(""))

scores = []

for i in range(0, n):
    scores.append(int(input("")))

scores.sort(reverse=True)

#print(scores)
'''
b_level = scores[2]
s_index = scores.index(b_level)
s_count = 0
i = 0
while True:
    if scores[s_index + i] == b_level:
        s_count += 1    
        i += 1
    else:
        break
#scores.count(b_level)
'''
first = scores[0]
second = 0
b_level = 0
s_count = 0

i = 0
while True:
    if scores[i] != first:
        second = scores[i]
        break
    i += 1


while True:
    if scores[i] != second:
        b_level = scores[i]
        break
    i += 1
#print(scores)
#print(first, second, b_level)
print(b_level, scores.count(b_level))
