import random
import shutil
import sys

def input_number(prompt):
    try:
        output = int(input(prompt))
        return output
    except ValueError:
        return False

def balance(bank, investment):
    bank = bank - investment
    return bank

monthly_wages_list = [2000, 2200, 2400, 2600]
monthly_wage = random.choice(monthly_wages_list)

monthly_expenses = [1200, 1400, 1600, 1800]

bank_balance = 1000
investment_balance = 0
rate = 0
default_rate = 2.5
total_months = 0

width = shutil.get_terminal_size((75, 20)).columns  
print('-' * width)
print('Welcome to Investment Simulator!')
print('-' * width)

while True:
    print('Your monthly wage is: $' + str(monthly_wage))
    months = 0
    print('Months passed:', total_months)
    print('Your current bank balance is: $' + str(bank_balance))

    while True:
        print('\nPlease choose and investment option:')
        print(' 1. Short-Term: 3 months @ 5% compounding interest per month')
        print(' 2. Medium-Term: 12 months @ 3% compounding interest per month')
        print(' 3. Long-Term: 24 months @ 1% compounding interest per month')
        print(' 4. Quit simulation')
        invest_choice = input_number('Choose: ')

        if invest_choice == 1:
            rate = 5
            duration = 3
            break
        elif invest_choice == 2:
            rate = 3
            duration = 12
            break
        elif invest_choice == 3:
            rate = 1
            duration = 24
            break
        elif invest_choice == 4:
            print('Goodbye!')
            sys.exit()
        else:
            print('Please choose option 1, 2, or 3. Enter 4 to exit.')
            continue

    invest_amount = input_number('\nPlease enter the amount you would like to invest: ')
    while True:
        if invest_amount > bank_balance:
            print('You do not have enouhg money for that investment amount!')
            continue
        else:
            break

    bank_balance = balance(bank_balance, invest_amount)

    invest_months = 0
    while True:
        invest_months += 1
        if invest_months <= (duration -1):
            invest_calc = invest_amount + (invest_amount/100) * rate
            print('\nMonth:', invest_months)
            print('Current balance: ', round(invest_calc, 2))
            invest_amount = invest_calc
        elif invest_months == duration:
            invest_calc = invest_amount + (invest_amount/100) * rate
            print('\nMonth:', invest_months)
            print('Closing balance: ', round(invest_calc, 2))
            print(f'\n{'-'*30}NEXT ROUND{'-'*30}')
            break

    investment_balance += invest_calc
    bank_balance += monthly_wage * duration

    print('Your total monthly wages for this ' + str(duration) + ' month period was: $' + str(bank_balance))
    monthly_expense = random.choice(monthly_expenses) * duration
    print('Your total monthly expenses for this ' + str(duration) + ' month period was: $' + str(monthly_expense) + '\n')

    bank_balance -= monthly_expense
    total_months += duration
