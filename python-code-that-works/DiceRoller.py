import random

#Define Yes/No stuff
listyes = ["y","Y", "yeah", "yeah mate", "yes", "Yes", "YES" ]
listno = ["n","N", "yeah nah", "no", "No", "NO"]

#Dice ASCII thing
number1 = """
 _________
/         \\
|         |
|    O    |
|         |
\_________/
"""
number2 = """
 _________
/         \\
|      O  |
|         |
|  O      |
\_________/
"""
number3 = """
 _________
/         \\
|      O  |
|    O    |
|  O      |
\_________/
"""
number4 = """
 _________
/         \\
|  O   O  |
|         |
|  O   O  |
\_________/
"""
number5 = """
 _________
/         \\
|  O   O  |
|    O    |
|  O   O  |
\_________/
"""
number6 = """
 _________
/         \\
|  O   O  |
|  O   O  |
|  O   O  |
\_________/
"""
listnumber = [number1,number2,number3,number4,number5,number6]


#Random integer
def rolldice():
    number = random.randint(0,5)
    print("\n\n\n\nThe dice rolls a: " + str(number+1) )
    print(listnumber[number])
    print("\n\n\n\n")
#User Input
def ask():
    print("Roll the dice?")
    global userinput
    userinput = input("(Y)es or (N)o: ")

#Logic
def loop():
    while userinput in listyes:
    
        if userinput in listyes :
            rolldice()
        
        elif userinput in listno:
            print("Goodbye!")
            break
        ask()    
        
    while userinput in listno:
        
        print("\nGoodbye!")
        break

ask()
loop()

while userinput not in listyes + listno:
    print("\nUnrecognised syntax")
    ask()
    loop()
        