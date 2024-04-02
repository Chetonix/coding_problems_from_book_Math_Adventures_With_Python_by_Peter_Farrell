
def average(a,b): 
    return (a + b)/2


def squareRoot(num,low,high): 
    '''Finds the square root of num by playing the Number Guessing Game strategy by guessing over the
range from "low" to "high"'''
    for i in range(30):
        guess = average(low,high) 
        if guess**2 == num:
            print(guess)
        elif guess**2 > num: #"Guess lower."
            high = guess
        else: #"Guess higher."
            low = guess 
    print(guess)
#squareRoot(60,7,8)
squareRoot(200, 10, 20)
squareRoot(1000, 1, 100)
squareRoot(50000, 100, 500)
