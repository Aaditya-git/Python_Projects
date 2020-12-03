print("WELCOME TO ROCK PAPER SCISSOR GAME!")
times=int(input("ENTER NUMBER OF TIMES YOU WANT TO PLAY:"))
print("========================================================\n\n")

chance=0
import random
import sys
while(chance<times):
    alist=["ROCK","PAPER","SCISSOR"]
    user_input=input("ENTER ROCK, PAPER or SCISSOR:").upper()
    if(user_input in alist):
        pass
    else :
        print("wrong input")
        continue
    computer=random.choice(alist)
    
    print("YOUR CHOICE WAS:-> {}".format(user_input))
    print("COMPUTER CHOSE :->{}".format(computer))
    
    if(user_input==computer):
        print('MATCH TIED!\n')
        
    elif(user_input=="ROCK" and computer=="PAPER"):
        print("COMPUTER WINS!\n")
     
    elif(user_input=="ROCK" and computer=="SCISSOR"):
        print("YOU WIN!\n")
        
    elif(user_input=="SCISSOR" and computer=="ROCK"):
        print("COMPUTER WINS!\n")
        
    elif(user_input=="SCISSOR" and computer=="PAPER"):
        print("YOU WIN!\n")
        
    elif(user_input=="PAPER" and computer=="SCISSOR"):
        print("COMPUTER WINS!\n")    
        
    elif(user_input=="PAPER" and computer=="ROCK"):
        print("YOU WIN!\n")
    
    chance=chance+1
     
    