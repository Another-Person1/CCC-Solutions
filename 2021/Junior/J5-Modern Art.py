row_num = int(input(""))
col_num = int(input(""))

choice_num = int(input(""))

row_set = set()
col_set = set()

for _ in range(choice_num):
    type_input, num = input().split()
    if type_input == 'R':
        if num in row_set:
            row_set.remove(num)
        else:
            row_set.add(num)
    elif type_input == 'C':
        if num in col_set:
            col_set.remove(num)
        else:
            col_set.add(num)

gold_num = len(row_set) * (col_num - len(col_set)) + len(col_set) * (row_num -len(row_set))

print(gold_num)
