import random

winning_number=random.randint(1,100)
guess_number=int(input("enter your number"))

count=1
flag=True

while flag:
    if guess_number==winning_number:
        print("You Win in {} Times ".format(count))
        flag=False

    elif guess_number<winning_number:
        print("enter above")

    elif guess_number>winning_number:
        print("enter below")


    count += 1
    guess_number = int(input("enter your number"))



