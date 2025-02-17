import time
import statistics # to calculate average

def rate_rhythm(target_time, actual_time):
    difference = abs(target_time - actual_time)
    percentage = (difference/target_time)*100
    if percentage <= 8:
        return 'Great!'
    elif percentage <= 16:
        return 'Okay!'
    elif percentage > 16:
        return 'Miss!'

print('Welcome to Rhythm Tester')
print('This program will test your rhythm - how consistent are YOU!')

while True:
    speed = input('Choose rhythm speed (1, 2, 3): ')
    if speed == '':
        print('Invalid choice. Enter 1, 2 or 3.')
    elif speed in '123': # valid inputs are stored in the string
        speed = int(speed) # converts and stores 'speed' as int
        break
    else:
        print('Invalid choice. Enter 1, 2 or 3.')

while True:
    rounds = input('Choose number of rounds (5 to 50): ')
    try:
        rounds = int(rounds) # converts and stores 'rounds' as int
    except ValueError:
        print('Invalid choice. Enter a whole number between 5 and 10.')
        continue
    if rounds >= 5 and rounds <=50:
        break

print('\nOkay, this test will last', rounds ,'rounds and you are aiming for a', speed ,'second rhythm')

response_list = []

while True: # check if user presses 'Enter' (empty string)
    print('Press Enter to begin!')
    enter = input('')
    if enter == '':
        break
    else:
        print("Press Enter to use program")
        
for i in range(rounds):
    start = time.time()
    input("Round " + str(i+1) + " of " + str(rounds))
    end = time.time()
    
    target_time = speed
    actual_time = end-start
    
    rate = rate_rhythm(target_time, actual_time)
    actual_time = round(actual_time, 2)
    print(str(actual_time) + 's - ' + str(rate) + '\n')
    response = (actual_time, rate) # store actual_time and rate in a tuple
    response_list.append(response)
    
results_input = input('Test Complete! Press Enter to see your results.\n')

if results_input == '': # if user presses 'Enter':
    print('Results:')

    fastest_response = min(response_list)
    print(' Fastest Response: ' + str(fastest_response[0]) + 's ' + '(' + fastest_response[1] + ')')

    responses = [i[0] for i in response_list] # creating a list for response times
    average_response = statistics.mean(responses)
    average_response = round(average_response, 2)
    print(' Average Response: ' + str(average_response) + 's ' + '(' + rate_rhythm(target_time, average_response) + ')')

    slowest_response = max(response_list)
    print(' Slowest Response: ' + str(slowest_response[0]) + 's ' + '(' + slowest_response[1] + ')\n')

    print('Round Response Difference')
    print('----- -------- ----------')
    for i in range(rounds):
        actual_difference = target_time - responses[i] # later will be used in early_late

        difference = round(abs(actual_difference), 2)
        difference = ("{:.2f}".format(difference))

        response = responses[i] # extracting the current response
        response = ("{:.2f}".format(response))

        if i < 9: # adjusting table column gap for 2 digit numbers
            space = '     '
        else:
            space = '    '
        if actual_difference == 0:
                print(str(i+1) + space + response + 's' + '    ' + 'Spot On!')
        else:
            if actual_difference > 0:
                early_late = 'early'
            else:
                early_late = 'late'
            print(str(i+1) + space + response + 's' + '    ' + difference + 's ' + str(early_late) + '.')
