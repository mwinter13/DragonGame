import random

def DragonGame():
    print('''Welcome to Dragon Land!  This is a place full of danger and adventure. 
Find the good dragon with a tremendous reward, and avoid being eaten! 

(press ENTER to continue)''')

    input()

    print('In front of you lie two caves- a large, grey cave and a smaller, red cave.  \
Which cave would you like to enter? (type "grey" to walk into the grey cave \
and type "red" to enter the red cave)')

    CaveInput = input()
    CaveInput = random.randint(1,5)
    if CaveInput == 1:
        print('Congratulations!!!  The dragon you\'ve encountered is friendly and gives you \
riches beyond your wildest dreams!')
    else:
        print('Oh no!  The dragon you\'ve encountered devoured you!  Game Over')

DragonGame()

while 1 == 1:
    print('would you like to play again? (type "y" to play again or "n" to stop playing)')
    Choice = input()
    if Choice == 'y':
        DragonGame()
    else:
        print('Thanks for playing!')
        break