n = input("")
d = input("")

n_list = list(n)
d_list = list(d)

silly = ''
silly_c = ''
quiet = '-'
good_keys = []
if len(n_list) == len(d_list):#quiet key not pressed
    for i in range(len(n_list)):
        if n_list[i] != d_list[i]:
            silly_c = n_list[i]
            silly = d_list[i]

else:# quiet key pressed
    
    for i in range(len(n_list)):
            if n_list[i] != d_list[i] and d_list[i] not in good_keys:
                silly_c = n_list[i]
                silly = d_list[i]
                good_keys.append(silly)
            
print(silly_c, silly)
print(quiet)
                