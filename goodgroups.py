from collections import defaultdict

x = int(input(""))
mustbeinsamegroup = defaultdict(list)
for i in range(x):
    student1, student2 = input().split()
    mustbeinsamegroup[student1].append(student2)

y = int(input(""))
mustnotbeinsamegroup = defaultdict(list)
i=0
for i in range(y):
    student1, student2 = input().split()
    mustnotbeinsamegroup[student1].append(student2)

g = int(input(""))
groups = []

for _ in range(g):
    groups.append(input().split())

#print(groups)
# constraint checking code
#print(mustbeinsamegroup, mustnotbeinsamegroup, groups)

violations = 0
for group in groups:
    for student in group:
        for mustbeinsamegroup_student in mustbeinsamegroup[student]:
            if mustbeinsamegroup_student not in group:
                violations += 1

        for mustnotbeinsamegroup_student in mustnotbeinsamegroup[student]:
            if mustnotbeinsamegroup_student in group:
                violations += 1            
print(violations)