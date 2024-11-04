import random

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
random.shuffle(numbers)
secret = numbers[:4]
print(secret)
guess = 0
result = []


while guess != ["green", "green", "green", "green"]:
    
    guess = input("enter a four digit number:   ")
    guess = list(guess)
    print(guess)

    for i in range (0, 4):
        if guess[i] == secret[i]:
            i = True
            result.append("green")
            
        if guess[i] != secret[i]:
            i = False
            result.append("red")

        elif guess[i] in secret[i]:
            result.append("yellow")

    print(result)
    
    


    
            
        

 

