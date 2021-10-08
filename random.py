import random
a = random.randrange(1, 10)
print("Try to guess what is this random number. ")
user_input = int(input())
while user_input != a:
    if user_input > a:
        print("Try lesser number")
        user_input = int(input())
    elif user_input < a:
        print("Try bigger number")
        user_input = int(input())
    if user_input == a:
        print("Congratulations!")