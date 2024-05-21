def find_troublesome_keys(pressed_keys, displayed_keys):
    silly_key = ''
    quiet_key = '-'
    wrong_letter = ''
    for i in range(len(pressed_keys)):
        if pressed_keys[i] != displayed_keys[i]:
            if silly_key == '':
                silly_key = pressed_keys[i]
                wrong_letter = displayed_keys[i]
            elif pressed_keys[i] != silly_key:
                quiet_key = pressed_keys[i]
    return silly_key, wrong_letter, quiet_key

# Test the function
pressed_keys = input("") #'abcde'
displayed_keys = input("") #'abade'
silly_key, wrong_letter, quiet_key = find_troublesome_keys(pressed_keys, displayed_keys)
print(f'{silly_key} {wrong_letter}')
print(quiet_key)