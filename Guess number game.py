#Guess number game


number=18

while(True):
    guess=int(input("Please enter a number: "))
    if guess < number:
        print("It is lesser than ",number," please try again to enter a number a little greater than ", number,"\n")
        continue
    elif guess > number:
        print("It is greater than ", number, " please try again to enter a number a little lesser than ", number,"\n")
        continue
    elif guess == number:
        print("Congratss!! you have successfully guessed the number.....")
        break
