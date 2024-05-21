def find_troublesome_keys(pressed_keys, displayed_keys):
    silly_key = None
    quiet_key = None
    wrong_letter = None

    for ch in pressed_keys:
        if ch not in displayed_keys:
            if silly_key == None:
                silly_key = ch
            elif ch != silly_key:
                quiet_key = ch
                break
    for ch in displayed_keys:
        if ch not in pressed_keys:
            wrong_letter = ch
            break
    if quiet_key:
        remove_quiet = pressed_keys.replace(quiet_key, '')
        replace_wrong = displayed_keys.replace(wrong_letter, silly_key)
        
        if remove_quiet !=  replace_wrong:
            silly_key, quiet_key = quiet_key, silly_key

    return silly_key, wrong_letter, quiet_key if quiet_key else '-'

# Test the function
pressed_keys = input("")
displayed_keys = input("")
silly_key, wrong_letter, quiet_key = find_troublesome_keys(pressed_keys, displayed_keys)
print(f'{silly_key} {wrong_letter}')
print(quiet_key)
