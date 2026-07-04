#  Guessing Game
def guessing():
    import random
    seceret_num = random.randint(1,10)
    attempts = 3
    while attempts>0:
        guess = int(input("Enter the guessing number:"))
        
        if guess> seceret_num:
            print("too high!")
        elif guess < seceret_num:
            print("Too low!")
        else:
            print("You won:")
            break
        attempts = attempts-1
        print("Wrong! Attempts:" , attempts)

    if attempts== 0:
        print(" 😘You lose!")
        print("The secret number was:", seceret_num)
guessing()