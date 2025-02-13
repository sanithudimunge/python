import random
import time

counter = 0
ran_num = None
total = 0
sev_count = 0

while ran_num != 0:
    counter += 1
    prv_num = ran_num
    if counter <= 20:
        ran_num = random.randint(0,10)
    elif counter > 20:
        ran_num = random.randint(0,5)

    #time.sleep(0.5) # Latency feature. comment this out for better testing.
    print('Number', counter, 'was', ran_num)
    total += ran_num # Calculating total

    # Game Over
    if counter == 1 and ran_num == 0:
        print(' * That was fast!')

    # Hot Streak
    if counter % 10 == 0:
        print(' *', counter, 'number streak!')

    # Lucky 7
    if ran_num == 7:
        print(' * Lucky 7!')

    # Match Count
    if counter == ran_num:
        print(' * Match Count!')

    # Snake Eyes
    if prv_num == ran_num:
        print(' * Snake Eyes!')

    # Slot Machine
    if ran_num == 7:
        sev_count += 1
        if sev_count == 3:
            print('777 Winner')
            break
    
    # Hotter Streak
    if counter == 20:
        print(' * Reducing range to 0-5')

print('\nTotal of Numbers:', total)
print('Average of Numbers:', round(total / counter, 2))
