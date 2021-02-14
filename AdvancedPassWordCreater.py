import random
"""
Descriptions:
    This is a project to create
    new password for your accounts
    that can be really hard to be hacked ;)))
"""

def passcreater(*args):
    select_arr = list()
    charDic = {
        0: range(97, 123), # the Range of LowerCase Characters
        1: range(65, 91), # the Range of UpperCase Characters
        2: range(48, 58), # the Range of Numbers
        3: [j for i, y in [(32, 48), (58, 65), (91, 97), (123, 127)] for j in range(i, y)], # the Range of Normal Symbols
        4: range(127, 1000) # the Range of Advanced Symbols
    }
    for index, state in enumerate(args[:-1]):
        if state:
            if index == 3:
                select_arr += charDic.get(3)
            else:
                select_arr += [i for i in charDic.get(index)]
    return ''.join([chr(random.choice(select_arr)) for i in range(args[-1])])

# Get The User's Desired Information about their wanted PassWord
def welcome():
    print("""Welcome to EFA Pass Creater
    Please Enter 'T' for Accept or 'F' to Ignore(Notice: writing any other thing will assume F too)""")
    gotten_data = []
    for i in ["lower aphabet", "upper alphabet", "numbers", "usual symbols", "advanced symbols"]:
        gotten_data.append(True if input(f" Would you like to have {i.capitalize()} in your PassWord? ").lower() == 't' else False)
    l = input("Please Enter the length of your desired PassWord: ")
    if l.isdigit():
        gotten_data.append(int(l))
        return passcreater(*gotten_data)
    else:
        print("Sorry length must be integer, Please try again")


t = welcome()
print(t)
# This program is writen by ESMAEIL FAKHERI ALAMDARI
