import random



input_number=random.randint(1,9)
chances=0
times=int(input("Enter number of chances you want:"))

while(chances<times):
    guess_number=int(input("Enter your GUESS between 1 to 9:"))
    
    if(guess_number==input_number):
        print("YOUR GUESS WAS RIGHT:")
        chances=chances+1
        break
    elif(guess_number<input_number):
        print("Enter a higher number than {} number".format(guess_number))
        chances=chances+1
        
    elif(guess_number>input_number):
        print("Enter a Lower number than {} number".format(guess_number))
        chances=chances+1
           
    if not(chances<times):
        print("You have lost,The number was {}".format(input_number))
input("press ENTER to exit")
    