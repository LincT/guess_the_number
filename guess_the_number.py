import random

correct = 'you guessed correctly!'
too_low = 'too low!!'
too_high = 'too high'
total_guesses = 0
error = 'invalid entry or out of range'

def configure_range():
    '''Set the high and low values for the random number'''
    return 1, 10

def increment_guesses():
    global total_guesses
    total_guesses=total_guesses+1

def display_guesses():
    print("You got it in ",total_guesses," guesses.")

def generate_secret(low, high):
    '''Generate a secret number for the user to guess'''
    return random.randint(low, high)


def get_guess():
    '''get user's guess'''
    userNumber = -1
    userInput = input('Guess the secret number? ')
    if userInput.isnumeric():
        userNumber = int(userInput)

    if configure_range()[0] <= userNumber <= configure_range()[1]:
        increment_guesses()
        return userNumber
    else:
        return -1


def check_guess(guess, secret):
    '''compare guess and secret, return string describing result of comparison'''
    if guess == secret:
        display_guesses()
        return correct
    elif guess == -1:
        return error
    elif guess < secret:
        return too_low
    elif guess > secret:
        return too_high


def main():

    (low, high) = configure_range()
    secret = generate_secret(low, high)

    while True:
        guess = get_guess()
        result = check_guess(guess, secret)
        print(result)

        if result == correct:
            break


if __name__ == '__main__':
    main()
