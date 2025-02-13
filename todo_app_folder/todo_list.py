def get_list(filename):
    try:
        file = open(filename, 'r')
        data = file.readlines()
        file.close()
    except FileNotFoundError:
        data = []
    return data

def show_list(data):
    if data == []:
        print('\nYour To Do List is empty.')
    else:
        print('\nTo Do List:')
        for index, item in enumerate(data):
            print(' ' + str(index+1) + ') ' + str(item.strip('\n')))

def add_to_list(filename, data):
    if data == []:
        element = input('Add: ')
    else:
        prompt = input('Add: ')
        element = '\n' + prompt

    data.append(element)

    file = open(filename, 'a')
    file.write(element)
    file.close()

    return data

def delete_from_list(filename, data):
    try:
        index = int(input('Item number to delete: '))
    except ValueError:
        print('Invalid item number.')
        return data

    try:
        if index < 1:
            raise IndexError
        del data[index-1]
    except IndexError:
        print('Invalid item number.')
    file = open(filename, 'w')
    file.writelines(data)
    file.close()

    return data

# --- main part of program ---
FILENAME = 'list.txt'
data = get_list(FILENAME)

while True:

    show_list(data)

    print('\nType "a" to add an item.')

    if data != []:
        print('Type "d" to delete an item.')

    print('Type "x" to exit.')

    command = input('> ')

    if command == 'a': 
        data = add_to_list(FILENAME, data)

    elif command == 'd' and data != []:
        data = delete_from_list(FILENAME, data)

    elif command == 'x':
        print('Goodbye!')
        break

    else:
        print('Invalid command.\n')
