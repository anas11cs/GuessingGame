import random

def computerGuess(lowval, highval, randNum, count=0):
    #DIVIDE AND CONQUER APPROACH
    if (highval>=lowval):
        guess=lowval+(highval-lowval)//2
        #If guess is in, what is in middle, its found !
        if(guess==randNum):
            return count
            #If "guess" is greater than the number,
            #Then next guess must be lesser then
            #Current number-guessed and lower value
        elif guess>randNum:
            count=count+1
            #Recursion
            return computerGuess(lowval,guess-1,randNum,count)
        else:
            count=count+1
            return computerGuess(guess+1,highval,randNum,count)
    else:
    #Can't find Number
        return -1
#Function Ends here

# ========

#generate a random number between 1 and 100
randNum = random.randint(1,101)

count =0
guess=-99

# Logic Below
while(guess!=randNum):
    # Get the user's guess
    guess=(int) (input("Enter your guess between 1 and 100:"))
    if guess < randNum:
        print("higher")
    elif guess > randNum:
        print("lower")
    else:
        print("You Guessed It!")
        break
    count=count+1
#end of while loop
print("You took "+str(count)+" steps to guess a number")
print("Computer took "+str(computerGuess(0,100,randNum))+" steps!")