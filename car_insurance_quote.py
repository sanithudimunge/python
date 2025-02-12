import shutil

print('Car Insurance Annual Quote')
quote = 0

while True:
    car_model = input('\nCar Make & Model: ')
    if car_model.strip() == '':
        print('Please enter a valid car model')
        continue
    break

while True:
    car_age = input('\nHow old is your car in years?: ')
    try:
        car_age = int(car_age)
        if car_age < 0:
            raise ValueError
    except ValueError:
        print('Please enter a valid number')
        continue
    if car_age < 1:
        quote += 400
    elif car_age < 5:
        quote += 300
    elif car_age < 10:
        quote += 200
    else:
        quote += 100
    break

while True:
    try:
        driver_age = input('\nHow old is the driver in years?: ')
        driver_age = int(driver_age)
        if driver_age < 0:
            raise ValueError
    except ValueError:
        print('Please enter a valid number')
        continue
    if driver_age < 19:
        quote += 400
    elif driver_age < 24:
        quote += 200
    elif driver_age < 26:
        quote += 100
    elif driver_age < 70:
        quote += 0
    else:
        quote += 200
    break

while True:
    parking_location = input('\nYou park in a [g]arage, [c]arport, [d]riveway, or on the [s]treet?: ')
    if parking_location not in ['g', 'c', 'd', 's']:
        print('Please enter a valid option')
        continue
    if parking_location == 'g':
        quote += 0
    elif parking_location == 'c':
        quote += 50
    elif parking_location == 'd':
        quote += 100
    elif parking_location == 's':
        quote += 150
    break

while True:
    prior_claims = input('\nHave you previously made an insurance claim? [yes] or [no]: ')
    if prior_claims not in ['yes', 'no']:
        print('Please enter a valid option')
        continue
    if prior_claims == 'yes':
        quote += 100
    elif prior_claims == 'no':
        quote -= 100
    break

print('\nHow many kilometers does your car travel annually?:')
print(' [1] Less than 10,000kms')
print(' [2] Between 10,000kms and 20,000kms')
print(' [3] More than 20,000kms')
while True:
    kms_travelled = input('Enter 1, 2 or 3: ')
    if kms_travelled not in ['1', '2', '3']:
        print('Please enter a valid option')
        continue
    if kms_travelled == '1':
        quote += 0
    elif kms_travelled == '2':
        quote += 150
    elif kms_travelled == '3':
        quote += 250
    break

print('\nSelect insurance policy:')
print(' [1] Third Party')
print(' [2] Third Party + Fire and Theft')
print(' [3] Comprehensive')
while True:
    insurance_policy = input('Enter 1, 2 or 3: ')
    if insurance_policy not in ['1', '2', '3']:
        print('Please enter a valid option')
        continue
    if insurance_policy == '1':
        quote += 100
    elif insurance_policy == '2':
        quote += 150
    elif insurance_policy == '3':
        quote += 300
    break

print('\nWhat is your membership level?: ')
print(' [1] Not a member')
print(' [2] Bronze Member')
print(' [3] Silver Member')
print(' [4] Gold Member')
while True:
    member_benefits = input('Enter 1, 2, 3 or 4: ')
    if member_benefits not in ['1', '2', '3', '4']:
        print('Please enter a valid option')
        continue
    if member_benefits == '1':
        quote -= 0
    elif member_benefits == '2':
        quote = quote - 2.5/100*quote
    elif member_benefits == '3':
        quote = quote - 5/100*quote
    elif member_benefits == '4':
        quote = quote - 7.5/100*quote
    break

print()

width = shutil.get_terminal_size((75, 20)).columns  

print('=' * width)
print('Insuring your ' + car_model + ' would cost $' + str(round(quote,2)))
print('=' * width)

if insurance_policy == '1':
    summary_policy = 'Third Party'
elif insurance_policy == '2':
    summary_policy = 'Third Party + Fire and Theft'
elif insurance_policy == '3':
    summary_policy = 'Comprehensive'

summary_car_age = car_age
summary_car_model = car_model
summary_quote = quote

if member_benefits == '1':
    summary_member_benefits = 'does not include a member discount'
elif member_benefits == '2':
    summary_member_benefits = 'includes a 2.5% Bronze member discount'
elif member_benefits == '3':
    summary_member_benefits = 'includes a 5% Silver member discount'
elif member_benefits == '4':
    summary_member_benefits = 'includes a 2.5% Gold member discount'

summary_driver_age = driver_age
if prior_claims == 'yes':
    summary_prior_claims = 'have not'
elif prior_claims == 'no':
    summary_prior_claims = 'have'

if parking_location == 'g':
    summary_parking_location = 'in a garage'
elif parking_location == 'c':
    summary_parking_location = 'in a carport'
elif parking_location == 'd':
    summary_parking_location = 'on a driveway'
elif parking_location == 's':
    summary_parking_location = 'on the street'

if kms_travelled == '1':
    summary_kms_travelled = 'less than 10,000kms'
elif kms_travelled == '2':
    summary_kms_travelled = '10,000kms - 20,000kms'
elif kms_travelled == '3':
    summary_kms_travelled = 'more than 20,000kms'

print(f'A {summary_policy} policy for your {summary_car_age} year old {summary_car_model} would cost ${summary_quote}.')
print(f'This {summary_member_benefits}.')

print('\nYou told us that:')
print(f' * You are {summary_driver_age} years old and {summary_prior_claims} made prior insurance claims.')
print(f' * The car is parked {summary_parking_location} and is driven {summary_kms_travelled} per year.')

print('=' * width)
