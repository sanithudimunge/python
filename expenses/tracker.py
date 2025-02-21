import pandas as pd

def new_record():
    date = input('Input YYYY-MM-DD: ')
    desc = input('Input Description: ')
    value = int(input('Value: '))
    data = {'Date': [date], 'Description': [desc], 'Value': [value]}

    df = pd.read_csv('expenses.csv') # read csv
    df = pd.DataFrame(data) # converts row into DataFrame
    df.to_csv('expenses.csv', mode='a', index=False, header=False) # add new row into csv

    df = pd.read_csv('expenses.csv')
    df['Date'] = pd.to_datetime(df['Date'])
    df_sorted = df.sort_values('Date')  # sort data in ascending order
    df_sorted.to_csv('expenses.csv', index=False)

    print('\nNew Record Added')

def delete_record():
    record_id = int(input('Enter index: '))
    df = pd.read_csv('expenses.csv')
    df = df.drop(index=record_id)
    df.to_csv('expenses.csv', index=False)
    print('\nRecord deleted')

def view_records():
    df = pd.read_csv('expenses.csv')
    print('\n'+str(df))

def daily_sums():
    df = pd.read_csv('expenses.csv')
    sums = df.groupby('Date')['Value'].sum()
    print('\n'+str(sums))

while True:
    print('\n1. New Record')
    print('2. Delete record')
    print('3. View records')
    print('4. Display daily sums')
    print('5. Exit program\n')

    select = input('Enter selection: ')

    if select == '1':
        new_record()

    elif select == '2':
        delete_record()

    elif select == '3':
        view_records()

    elif select == '4':
        daily_sums()

    elif select == '5':
        print('Exited program...')
        break;

    else:
        print('Invalid input')
