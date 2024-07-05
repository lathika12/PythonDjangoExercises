import random

def get_random():
    num = int(random.random()*1000)
    if len(set(str(num))) < 3:
        num = num + 123
        print("setting unique num", num)
    return num

def __main__():
    """
    Match - Nope - Close
    Close - Guessed a number right - wrong position
    Match - Guessed a number right and right position
    Nope - nothing correct
    :return: nothing
    """
    print("Please guess your number")
    rn = get_random()
    ls = [int(i) for i in str(rn)]
    b = True

    while b:
        n = int(input("Enter your value: "))
        guess = [int(i) for i in str(n)]

        if n == rn:
            print("Congratulations! You guessed the number: {num}".format(num=n))
            b = False

        if guess[0] == ls[0] or guess[1] == ls[1] or guess[2] == ls[2]:
            print("MATCH!")
        elif guess[0] in ls or guess[1] in ls or guess[2] in ls:
            print("CLOSE!")
        else:
            print("NOPE! Try again")

__main__()