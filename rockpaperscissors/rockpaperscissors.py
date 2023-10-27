def gt_input():
    choice = input("Enter your choice for rock paper scissors:")
    if(choice.isalpha() == True):
        choice = choice.upper()
    else:
        print("Invalid")
        return gt_input()

    if(choice == "R" or choice == "P" or choice == "S" ):
        return choice
    else:
        print("Invalid")
        return gt_input()

def fn_rps(a,b):
    if(a==b):
        print("Tie")
    elif(a == "R" and b == "S") or (a == "P" and b == "R") or (a == "S" and b == "P"):
        print("Player A wins")
    else:
        print("Player B wins")

player_A = gt_input()
player_B = gt_input()

fn_rps(player_A,player_B)
