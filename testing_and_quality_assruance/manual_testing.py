def calculate_tax(income):
    income = int(income)
    if income <= 18200:
        tax = 0
    elif income <= 37000:
        tax = (income - 18200) * 0.19
    elif income <= 90000:
            tax = 3572 + (income - 37000) * 0.325
    elif income <= 180000:
        tax = 20797 + (income - 900000) * 0.37 # 1 extra zero in '90,000' detected
    else:
        tax = 54097 + (income - 180000) * 0.45
    return round(tax, 2)

def fixed_value_calculate_tax(income):
    income = int(income)
    if income <= 18200:
        tax = 0
    elif income <= 37000:
        tax = (income - 18200) * 0.19
    elif income <= 90000:
            tax = 3572 + (income - 37000) * 0.325
    elif income <= 180000:
        tax = 20797 + (income - 90000) * 0.37 # fixed to '90,000'
    else:
        tax = 54097 + (income - 180000) * 0.45
    return round(tax, 2)

def fixed_calculate_tax(income):
    income = round(float(income)) # only fix
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


# boundaries: 0, 18200, 18201, 37000, 37001, 90000, 90001, 180000, 180001
# considering boundaries to be inputs, unexpected input types:
    # negative int ('-1')
    # int with whitespace around (' 5700 ')
    # float ('27000.75')
    # string with letters ('hello world')
    # entire whitespace ('      ')
    # nothing ('')

# prompt for input
income = input('What is your taxable income?: ')

try:
    # call function and store the result
    tax = calculate_tax(income)

    # print the result with 2 decimal places
    print('using flawed program:', format(tax, '.2f'))
except ValueError:
    print('using flawed program:', 'ValueError')

try:
    fixed_value_tax = fixed_value_calculate_tax(income)
    print('using fixed_val program:', format(fixed_value_tax, '.2f'))
except ValueError:
    print('using fixed_val program:', 'ValueError')

try:
    fixed_tax = fixed_calculate_tax(income)
    print('using fixed program:', format(fixed_tax, '.2f'))
except ValueError:
    print('using fixed program:', 'ValueError')

# Manually testing the boundaries and edge cases and entering the results manually
value_results = {
    'Input          ': [0, 18200, 18201, 37000, 37001, 90000, 90001, 180000, 180001],
    'Expected output': [0.00, 0.00, 0.19, 3572.00, 3572.33, 20797.00, 20797.37, 54097.00, 54097.45],
    'Actual output  ': [0.00, 0.00, 0.19, 3572.00, 3572.32, 20797.00, -278902.63, -278902.63, 54097.45],
    'Test Result    ': ['Pass', 'Pass', 'Pass', 'Pass', 'Fail*', 'Pass', 'Fail', 'Fail', 'Pass']
}
# actual output = flawed program output
# Fail* 5th input fail happenned due to how different languages round values

type_results = {
    'Input          ': ['-1', '  57000  ', '27000.75', 'hello world', '      ', ''],
    'Expected output': [0.00, 10072, 1672.19, ValueError, ValueError, ValueError],
    'Actual output  ': [0.00, 10072, ValueError, ValueError, ValueError, ValueError],
    'Test Result    ': ['Pass', 'Pass', 'Fail', 'Pass', 'Pass', 'Pass']
}