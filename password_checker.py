def check_password(pword):
    short_enough = False
    long_enough = False
    has_upper = False
    has_lower = False
    has_number = False
    has_special = False

    special_chars = '\'~!#$%^*()_+-={}|[]\\:<>?,./'


    if len(pword) <= 16:
        short_enough = True
    if len(pword) >= 8:
        long_enough = True
    
    for char in pword:
        if char.isupper():
            has_upper = True
        if char.islower():
            has_lower = True
        if char.isdigit():
            has_number = True
        if char in special_chars:
            has_special = True
    if short_enough and long_enough and has_upper and has_lower and has_number and has_special:
        return True
    else:
        return False

# optimized version
def better_check_password(pword):
    short_enough = False
    long_enough = False
    has_upper = False
    has_lower = False
    has_number = False
    has_special = False

    special_chars = '\'~!#$%^*()_+-={}|[]\\:<>?,./'

    if len(pword) <= 16:
        short_enough = True
    if len(pword) >= 8:
        long_enough = True
    if not (short_enough and long_enough):
        return False # immediate return
    
    for char in pword:
        # optimized if-conditions
        # example: if current char in loop has_upper=True, the condition becomes false regardless of the other condition
        # (not has_upper=False)
        if not has_upper and char.isupper():
            has_upper = True
        elif not has_lower and char.islower():
            has_lower = True
        elif not has_number and char.isdigit():
            has_number = True
        elif char in special_chars:
            has_special = True
        if has_upper and has_lower and has_number and has_special:
            return True # immediate return if all loop vars are true
    if short_enough and long_enough and has_upper and has_lower and has_number and has_special:
        return True
    else:
        return False

password = input('Enter your password: ')

print('\nUsing password checker1')
if check_password(password):
    print('Your password is valid.')
else:
    print('Your password is invalid.')

print('\nUsing password checker2')
if better_check_password(password):
    print('Your password is valid.')
else:
    print('Your password is invalid.\n')