instructions = input("")

for i in range(len(instructions)):
    if instructions[i] == "+":
        print(" tighten ", end='')
    elif instructions[i] == "-":
        print(" loosen ", end='')
    elif instructions[i].isalpha():
        print(instructions[i], end='')
    else:
        print(instructions[i], end='')
        try:
            if instructions[i+1].isdigit() == False:
                print("")
        except:
            print("")
            exit()
