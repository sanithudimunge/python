def validate_tfn(tfn):
    tfn_list = list(map(int, tfn))
    weight_list = [1, 4, 3, 7, 5, 8, 6, 9, 10]

    full_total = 0
    for i in range(9):
        col_total = tfn_list[i] * weight_list[i]
        full_total += col_total

    if full_total % 11 == 0:
        return True
    else:
        return False

# Main Loop
while True:
    tfn = input('Enter your Tax File Number: ')
    tfn = tfn.replace(' ', '')
    try:
        int(tfn)
        if len(tfn) != 9:
            raise ValueError
        break
    except:
        print('Invalid input')

if validate_tfn(tfn) == True:
    print('Valid Tax File Number')
else:
    print('Invalid Tax File Number')


# 1st 10 Valid Tax File Numbers
'''
valids = 0
tfn = 0

while valids <= 10:
    if validate_tfn(f'{tfn:09d}') == True:
        print(f'{tfn:09d}')
        valids += 1
    tfn = int(tfn) + 1
'''

# Last 10 Valid Tax File Numbers
'''
valids = 0
tfn = 999999999

while valids <= 10:
    if validate_tfn(f'{tfn:09d}') == True:
        print(f'{tfn:09d}')
        valids += 1
    tfn = int(tfn) - 1
'''