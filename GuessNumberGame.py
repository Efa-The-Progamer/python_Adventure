import random
"""
Descriptions:
    This is a game witch takes a range number from user
    and creates a random number and user
    has to guess that number.
Notice:
    user doesn't has any time or guess limit.
"""


def guessgame(end=100):
    random_number = random.randint(0, end)
    print('if you need help, print "help"')
    while True:
        inp = input(f'Please Enter A Number between [0, {end}]: ').lower()
        if inp == 'exit':
            return True
        elif inp == 'answer':
            print(random_number)
            continue
        elif inp == 'help':
            print("""type 'answer' to get answer
            type 'exit' to quit the game""")
        elif inp == str(random_number):
            print('Congratulation, You Won')
            return True
        else:
            if not inp.isdigit():
                print('WARNNING!!!, Please Enter an Integer Number Or "help" Or "answer" Or "exit"')
            else:
                d = random_number - int(inp)
                if d < 0:
                    print('Sorry, It is High')
                else:
                    print('Sorry, It is Low')


print("""Welcome to Guess Number Game created by E.F.A""")
i = input("Please Enter the range of numbrers you want to predict , 0 until: ")
if i.isdigit():
    guessgame(int(i))
else:
    print('WARNNING!!!, Please Enter an Integer Number')
# This Project is created by ESMAEIl FAKHERI ALAMDARI  (E.F.A)
