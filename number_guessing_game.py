import random

def input_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print('Please enter an integer')

print('Pick a range of numbers to guess from (integers only): ')

range_min = input_int('Pick the minimum number of range: ')
range_max = input_int('Pick the maximum number of range: ')

range_rand = random.randint(range_min, range_max)

print('\nRandom number assigned.')
print('Guess the number from', range_min, 'to', range_max)

while True:
    guess = input_int('\nEnter your guess: ')
    if guess < range_rand:
        print('Too low')
    elif guess > range_rand:
        print('Too high')
    elif guess == range_rand:
        print('You guessed correctly!\n')
        break
