import random

def gt_input():
    money = input("Enter your how much money you have $")
    if(money.isnumeric() == True):
        return int(money)
    else:
        print("Invalid")
        return gt_input()


def fn_craps(x):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)

    if(x>=1):
        if(dice1+dice2 == 7):
            print("You won")
            x = 1.5*x
            print("You now have",x,"dollars")
            return fn_craps(x)
        else:
            print("You lost")
            x = 0.5*x
            print("You now have",x,"dollars")
            return fn_craps(x)
    else:
        print("You lost all your money")


def count_games():
    counter = 1
    while counter > 0:
        numberOfgames = counter + 1
        print("You won %d game or games before losing" % numberOfgames)
        break



bet = gt_input()
fn_craps(bet)
count_games()
