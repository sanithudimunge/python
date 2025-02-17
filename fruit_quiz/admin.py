import json

# This function repeatedly prompts for input until something other than whitespace is entered.
# Takes in a custom prompt, and prompts until non-whitespace inputs are entered
def input_something(prompt):
    while True:
        user_input = input(prompt)
        if user_input.strip() != '':
            return user_input

# This function repeatedly prompts for input until a float with a minimum of 0 is entered.
# Takes in a custom prompt, and prompts until a positive number is entered.
def input_float(prompt):
    while True:
        user_input = input(prompt)

        try:
            if float(user_input)<0:
                raise ValueError
        except ValueError:
            print('Invalid input. Enter a valid positive number')
            continue

        return user_input 

# This function opens "data.txt" in write mode and writes the data to it in JSON format.
# Saves data in JSON format.
def save_data(data):
    file = open('data.txt', 'w')
    json.dump(data, file)
    file.close()

# Try to open file. 'data' list will be empty if file doesn't exist or contains invalid JSON format.
try:
    file = open('data.txt', 'r')
    data = json.load(file)
    file.close()
except FileNotFoundError:
    data = []
except json.JSONDecodeError:
    data = []


print('Welcome to the Fruit Quiz Admin Program.')

while True:
    print('\nChoose [a]dd, [l]ist, [s]earch, [v]iew, [d]elete or [q]uit.')
    choice = input('> ').lower()
        
    if choice == 'a':
        # Add a new fruit.
        # Calling 'input_something' function to input 'fruit_name'.
        fruit_name = input_something('Enter fruit name: ')

        # Check if 'fruit_name' is already included.
        exists=False
        for item in range(len(data)):
            if data[item]["name"].lower() == fruit_name.lower():
                exists = True
        if exists == True:
            print('"' + fruit_name + '" already exists in data.')
            continue

        # Prompt for fruit information using 'input_float' function.
        print('In 100 grams of ' + fruit_name + ', how many...')

        fruit_energy = input_float('Calories are there?: ')

        fruit_fibre = input_float('Grams of fibre are there?: ')

        fruit_sugar = input_float('Grams of sugar are there?: ')

        fruit_potassium = input_float('Milligrams of potassium are there?: ')

        fruit_info = {"name": fruit_name,
                      "energy": fruit_energy,
                      "fibre": fruit_fibre,
                      "sugar": fruit_sugar,
                      "potassium": fruit_potassium}

        # Update 'data' list with fruit information.
        data.append(fruit_info)
        save_data(data)

        print('Fruits added!')
    
    elif choice == 'l':
        # List the current fruit.
        # Prints list of fruits in 'data' list with index.
        if data == []:
            print("No fruit saved")
        else:
            print('List of fruit:')
            for index, fruit in enumerate(data):
                print(' ' + str(index+1) + ') ' + fruit["name"])

    elif choice == 's':
        # Search the current fruit.
        if len(data) == 0:
            print("No fruit saved")

        # Call 'input_something' to prompt search terms and display seaerch results with index.
        else:
            search = input_something('Enter search term: ').lower()
            available = False
            print('Search results:')
            for index, fruit in enumerate(data):
                if search in (fruit["name"].lower()):
                    available = True
                    print(' ' + str(index+1) + ') ' + fruit["name"])
                    
            if available == False:
                print('No results found')
                
    elif choice == 'v':
        # View a fruit.
        if data == []:
            print('No fruit saved')

        else:
            # Error handling for fruit index input
            try:
                index = int(input('Fruit number to view: '))
                if index > len(data):
                    raise ValueError
            except ValueError:
                print('Invalid index number')
                continue

            # Print fruit information for fruit index
            index = index-1
            print('Nutritional information for 100 grams of ' + data[index]["name"])
            print(' Energy: ' + data[index]["energy"] + ' calories')
            print(' Fibre: ' + data[index]["fibre"] + ' grams')
            print(' Sugar: ' + data[index]["sugar"] + ' grams')
            print(' Potassium: ' + data[index]["potassium"] + ' milligrams')                
                
    elif choice == 'd':
        # Delete a fruit.

        if data == []:
            print("No fruit saved.")
        else:
            # Error handling for fruit index input
            try:
                index = int(input("Fruit number to delete: "))
                if index > len(data):
                    raise ValueError
            except ValueError:
                print("Invalid index number.")
                continue

            # Deleting fruit for fruit index
            data.pop(index - 1)
            save_data(data)
            print("Fruit deleted.")

    
    elif choice == 'q':
        # Quit the program.
        print('Goodbye!')
        break
        
    else:
        # Print "invalid choice" message.
        print('invalid choice')
