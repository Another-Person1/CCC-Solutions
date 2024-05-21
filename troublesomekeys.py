n = input("")
d = input("")

n_list = list(n)
d_list = list(d)

silly = ''
silly_c = ''
quiet = '-'
if len(n_list) == len(d_list):#quiet key not pressed
    for i in range(len(n_list)):
        if n_list[i] != d_list[i]:
            silly_c = n_list[i]
            silly = d_list[i]
else:
    

print(silly_c, silly)
print(quiet)
