import random

correct = 'you guessed correctly!'
too_low = 'too low'
too_high = 'too high'
error = 'out of range'


def configure_range():
    '''Set the high and low values for the random number'''
    return 1, 10


def generate_secret(low, high):
    '''Generate a secret number for the user to guess'''
    return random.randint(low, high)


def get_guess():
    '''get user's guess'''
    userInput = input('Guess the secret number? ')
    if str(userInput).isnumeric():
        if int(userInput) in range(configure_range()[1]):
            return int(userInput)
        else:
            return -1
    else:
        return -1


def check_guess(guess, secret):
    '''compare guess and secret, return string describing result of comparison'''
    if guess == secret:
        return correct
    if guess == -1:
        return error
    if guess < secret:
        return too_low
    if guess > secret:
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
