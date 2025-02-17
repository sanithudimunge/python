def calculate_tax(income): # fixed
    income = round(float(income))
    if income <= 18200:
        tax = 0
    elif income <= 37000:
        tax = (income - 18200) * 0.19
    elif income <= 90000:
            tax = 3572 + (income - 37000) * 0.325
    elif income <= 180000:
        tax = 20797 + (income - 90000) * 0.37
    else:
        tax = 54097 + (income - 180000) * 0.45
    return round(tax, 2)


value_tests = [
    {'desc': 'Boundary 0', 'input': 0, 'expected': 0.00},
    {'desc': 'Boundary 18200', 'input': 18200, 'expected': 0.00},
    {'desc': 'Boundary 18201', 'input': 18201, 'expected': 0.19},
    {'desc': 'Boundary 37000', 'input': 37000, 'expected': 3572.00},
    {'desc': 'Boundary 37001', 'input': 37001, 'expected': 3572.33},
    {'desc': 'Boundary 90000', 'input': 90000, 'expected': 20797.00},
    {'desc': 'Boundary 90001', 'input': 90001, 'expected': 20797.37},
    {'desc': 'Boundary 180000', 'input': 180000, 'expected': 54097.00},
    {'desc': 'Boundary 180001', 'input': 180001, 'expected': 54097.45}
]

print('Value test')
for index, test in enumerate(value_tests):
    desc = test['desc']
    actual_tax = calculate_tax(test['input'])

    if actual_tax == test['expected']:
        pass_fail = 'Test passed'
    else:
        pass_fail = 'Test failed'
    
    print('Test ' + str(index+1) + ' (' + desc + ')' + ': ' + pass_fail + ' (Res: ' + format(actual_tax, '.2f') + ', Exp: ' + format(test['expected'], '.2f') + ')')

type_tests = [
    {'desc': 'Negative Int', 'input': -1, 'expected': 0.00},
    {'desc': 'Int & Whitespace', 'input': ' 57000 ', 'expected': 10072.00},
    {'desc': 'Float', 'input': 27000.75, 'expected': 1672.19},
    {'desc': 'String', 'input': 'heaps of money', 'expected': ValueError},
    {'desc': 'All Whitespace', 'input': ' ', 'expected': ValueError},
    {'desc': 'Nothing', 'input': '', 'expected': ValueError}
]

print('\nType test')
for index, test in enumerate(type_tests):
    desc = test['desc']
    try:
        actual_tax = calculate_tax(test['input'])
        actual_tax = format(actual_tax, '.2f')
    except Exception as ex:
        actual_tax = type(ex)
    try:
        if str(actual_tax) == format(test['expected'], '.2f'):
            pass_fail = 'Test passed'
        else:
            pass_fail = 'Test failed'
    except Exception as ex:
        if actual_tax == test['expected']:
            pass_fail = 'Test passed'
        else:
            pass_fail = 'Test failed'
    actual_tax = str(actual_tax)
    print('Test ' + str(index+1) + ' (' + desc + ')' + ': ' + pass_fail + ' (Res: ' + actual_tax + ', Exp: ' + str(test['expected']) + ')')
