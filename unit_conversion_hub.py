import sys

# definitions
# length
length_units_list = ['km', 'm', 'cm','mm','mi', 'yd', 'ft', 'in']

# mass
mass_units_list = ['kg','g', 'mg', 'lb', 'oz']

# volume
vol_units_list = ['l', 'ml', 'gal', 'fl oz', 'c']

# speed
speed_units_list = ['kmph', 'mps', 'mph']

# temperature
temp_units_list = ['c', 'f', 'k']

# Time
time_units_list = ['s', 'min', 'hr', 'day', 'week', 'month', 'year']

def input_option(options_list):
    while True:
        option = input('Enter option (press x to exit): ').lower()
        if option == 'x':
            print('Exiting program.')
            sys.exit()
        elif option in options_list:
            return option
        else:
            print('Please select a valid option.')

def input_value(from_unit):
    while True:
        value = input('Enter value in ' + from_unit + ' (press x to exit): ').lower()
        if value == 'x':
            print('Exiting program.\n')
            sys.exit()
        try:
            value = float(value)
            return value
        except ValueError:
            print('Please enter a valid number.')

# 60km to m
def calculate_conversion(from_value, from_unit, to_unit, units_list):
    if units_list == length_units_list:
        # length_units_list = ['km','m', 'cm','mm','mi', 'yd', 'ft', 'in']
        length_conversion_list = [1000, 1, 0.01, 0.001, 1609.34, 0.9144, 0.3048, 0.0254]
        to_metres_value = from_value * length_conversion_list[units_list.index(from_unit)] # to metres
        to_value = to_metres_value / length_conversion_list[units_list.index(to_unit)] # to to_unit
        return to_value

    elif units_list == mass_units_list:
        # mass_units_list = ['kg','g', 'mg', 'lb', 'oz']
        mass_conversion_list = [1, 0.001, 0.000001, 2.205, 35.274]
        to_kg_value = from_value * mass_conversion_list[units_list.index(from_unit)] # to kilograms
        to_value = to_kg_value / mass_conversion_list[units_list.index(to_unit)] # to to_unit
        return to_value

    elif units_list == vol_units_list:
        # volume_units_list = ['l','ml', 'gal', 'fl oz', 'c']
        volume_conversion_list = [1, 0.001, 0.264172, 33.814, 4.167]
        to_litres_value = from_value * volume_conversion_list[units_list.index(from_unit)] # to litres
        to_value = to_litres_value / volume_conversion_list[units_list.index(to_unit)] # to to_unit
        return to_value
    
    elif units_list == speed_units_list:
        # speed_units_list = ['kmph', 'mps', 'mph']
        speed_conversion_list = [0.277, 1, 0.447]
        to_mps_value = from_value * speed_conversion_list[units_list.index(from_unit)] # to metres per second
        to_value = to_mps_value / speed_conversion_list[units_list.index(to_unit)] # to to_unit
        return to_value
    
    elif units_list == temp_units_list:
        # temp_units_list = ['c', 'f', 'k']
        temp_conversion_list = [from_value, (from_value-32)*5/9, from_value-273.15]
        to_celcius_value = from_value * temp_conversion_list[units_list.index(from_unit)] # to kelvin
        to_value = to_celcius_value / temp_conversion_list[units_list.index(to_unit)] # to to_unit
        return to_value
    
    elif units_list == time_units_list:
        # time_units_list = ['s', 'min', 'hr', 'day', 'week', 'month', 'year']
        time_conversion_list = [0.1666, 1, 60, 1440, 10080, 43800, 525600]
        to_min_value = from_value * time_conversion_list[units_list.index(from_unit)] # to minutes
        to_value = to_min_value / time_conversion_list[units_list.index(to_unit)] # to to_unit
        return to_value


print('\nUNIT CONVERSION HUB\n')

print('* Sections:')
print(' [1] Length')
print(' [2] Mass / Weight')
print(' [3] Volume')
print(' [4] Speed')
print(' [5] Temperature')
print(' [6] Time')

print('\n [s] Direct Search\n')

menu_options = ['1', '2', '3', '4', '5', '6', 's']
menu_input = input_option(menu_options)

# Length
if menu_input == '1':
    # Length from
    print('\n* Length:')
    print('List of units to convert from:')
    print(' [km] kilometres')
    print(' [m] metres')
    print(' [cm] centimetres')
    print(' [mm] millimetres')
    print(' [mi] miles')
    print(' [yd] yards')
    print(' [ft] feet')
    print(' [in] inches')

    print('\nWhat unit would you like to convert from?')
    length_from_unit = input_option(length_units_list)

    # Length to
    print('\n* Length:')
    print('List of units to convert to:')
    print(' [km] kilometres')
    print(' [m] metres')
    print(' [cm] centimetres')
    print(' [mm] millimetres')
    print(' [mi] miles')
    print(' [yd] yards')
    print(' [ft] feet')
    print(' [in] inches')

    print('\nWhat unit would you like to convert to?')
    length_to_unit = input_option(length_units_list)

    # Length conversion
    print('\n* Length:')
    print(length_from_unit, '→', length_to_unit, 'Conversion')
    length_from_value = input_value(length_from_unit)
    length_to_value = calculate_conversion(length_from_value, length_from_unit, length_to_unit, length_units_list)
    print(length_to_value, length_to_unit)

# Mass / Weight
elif menu_input == '2':
    # Mass from
    print('\n* Mass / Weight:')
    print('List of units to convert from:')
    print(' [kg] kilograms')
    print(' [g] grams')
    print(' [mg] milligrams')
    print(' [lb] pounds')
    print(' [oz] ounces')

    print('\nWhat unit would you like to convert from?')
    mass_from_unit = input_option(mass_units_list)
    
    # Mass to
    print('\n* Mass / Weight:')
    print('List of units to convert to:')
    print(' [kg] kilograms')
    print(' [g] grams')
    print(' [mg] milligrams')
    print(' [lb] pounds')
    print(' [oz] ounces')

    print('\nWhat unit would you like to convert to?')
    mass_to_unit = input_option(mass_units_list)

    # Mass conversion
    print('\n* Mass / Weight:')
    print(mass_from_unit, '→', mass_to_unit, 'Conversion')
    mass_from_value = input_value(mass_from_unit)
    mass_to_value = calculate_conversion(mass_from_value, mass_from_unit, mass_to_unit, mass_units_list)
    print(mass_to_value, mass_to_unit)

# Volume
elif menu_input == '3':
    # Volume
    print('\n* Volume:')
    print('List of units to convert from:')
    print(' [l] litres')
    print(' [ml] millilitres')
    print(' [gal] gallons')
    print(' [fl oz fluid ounces')
    print(' [c] cups')

    print('\nWhat unit would you like to convert from?')
    vol_from_unit = input_option(vol_units_list)

    # Volume to
    print('\n* Volume:')
    print('List of units to convert to:')
    print(' [l] litres')
    print(' [ml] millilitres')
    print(' [gal] gallons')
    print(' [fl oz fluid ounces')
    print(' [c] cups')

    print('\nWhat unit would you like to convert to?')
    vol_to_unit = input_option(vol_units_list)

    # Mass conversion
    print('\n* Volume:')
    print(vol_from_unit, '→', vol_to_unit, 'Conversion')
    vol_from_value = input_value(vol_from_unit)
    vol_to_value = calculate_conversion(vol_from_value, vol_from_unit, vol_to_unit, vol_units_list)
    print(vol_to_value, vol_to_unit)

# Speed
elif menu_input == '4':
    # Speed from
    print('\n* Speed:')
    print('List of units to convert from:')
    print(' [kmph] kilometres per hour')
    print(' [mps] metres per second')
    print(' [mph] miles per hour')

    print('\nWhat unit would you like to convert from?')
    speed_from_unit = input_option(speed_units_list)

    # Speed to
    print('\n* Speed:')
    print('List of units to convert to:')
    print(' [kmph] kilometres per hour')
    print(' [mps] metres per second')
    print(' [mph] miles per hour')

    print('\nWhat unit would you like to convert to?')
    speed_to_unit = input_option(speed_units_list)

    # Speed conversion
    print('\n* Speed:')
    print(speed_from_unit, '→', speed_to_unit, 'Conversion')
    speed_from_value = input_value(speed_from_unit)
    speed_to_value = calculate_conversion(speed_from_value, speed_from_unit, speed_to_unit, speed_units_list)
    print(speed_to_value, speed_to_unit)

# Temperature
elif menu_input == '5':
    # Temperature from
    print('\n* Temperature:')
    print('List of units to convert from:')
    print(' [c] celsius')
    print(' [f] fahrenheit')
    print(' [k] kelvin')

    print('\nWhat unit would you like to convert from?')
    temp_from_unit = input_option(temp_units_list)

    # Temperature to
    print('\n* Speed:')
    print('List of units to convert to:')
    print(' [c] celsius')
    print(' [f] fahrenheit')
    print(' [k] kelvin')

    print('\nWhat unit would you like to convert to?')
    temp_to_unit = input_option(temp_units_list)

    # Speed conversion
    print('\n* Temperature:')
    print(temp_from_unit, '→', temp_to_unit, 'Conversion')
    temp_from_value = input_value(temp_from_unit)
    temp_to_value = calculate_conversion(temp_from_value, temp_from_unit, temp_to_unit, temp_units_list)
    print(temp_to_value, temp_to_unit)

# Time
elif menu_input == '6':
    # Time from
    print('\n* Time:')
    print('List of units to convert from:')
    print(' [s] seconds')
    print(' [min] minutes')
    print(' [hr] hours')
    print(' [day] days')
    print(' [week] weeks')
    print(' [month] months')
    print(' [year] years')

    print('\nWhat unit would you like to convert from?')
    time_from_unit = input_option(time_units_list)

    # Time to
    print('\n* Time:')
    print('List of units to convert to:')
    print(' [s] seconds')
    print(' [min] minutes')
    print(' [hr] hours')
    print(' [day] days')
    print(' [week] weeks')
    print(' [month] months')
    print(' [year] years')

    print('\nWhat unit would you like to convert to?')
    time_to_unit = input_option(time_units_list)

    # Time conversion
    print('\n* Time:')
    print(time_from_unit, '→', time_to_unit, 'Conversion')
    time_from_value = input_value(time_from_unit)
    time_to_value = calculate_conversion(time_from_value, time_from_unit, time_to_unit, time_units_list)
    print(time_to_value, time_to_unit)

elif menu_input == 's':
    all_units_list = [length_units_list, mass_units_list, vol_units_list, speed_units_list, temp_units_list, time_units_list]
    current_unit_list = []
    while True:
        search_from_unit = input('What unit would you like to convert from? ')
        for unit_list in all_units_list:
            if search_from_unit in unit_list:
                current_unit_list = unit_list
                break
        if current_unit_list == []:
            print('Unit not found.')
        else:
            break
    print(current_unit_list)
    while True:
        search_to_unit = input('What unit would you like to convert to? ')
        if search_to_unit in current_unit_list:
            break
        else:
            print('Invalid conversion.')
    search_from_value = input_value(search_from_unit)
    search_to_value = calculate_conversion(search_from_value, search_from_unit, search_to_unit, current_unit_list)
    print(search_to_value)