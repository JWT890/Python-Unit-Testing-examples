def fn_single_number(number):
    print("Pay the number",number)

def fn_odd_vs_even_number(number):
    if(number%2==0):
        print("Pay odd")
    else:
        print("Pay even")

def fn_half_board(number):
    if(number>=1 and number <= 18):
        print("Pay 1 to 18")
    else:
        print("Pay 19 to 36")

def fn_red_vs_black(number):
    if(number==0):
        print("")
    else:
        if(number >= 1 and number <=9 and number%2==1):
            print("Pay red")
        elif(number>=12 and number <=18 and number%2==0):
            print("Pay red")
        elif(number>=21 and number <=27 and number%2==1):
            print("Pay red")
        elif(number>=30 and number <=36 and number%2==0):
            print("Pay red")
        else:
            print("Pay black")

def fn_game(number):
    fn_single_number(number)
    fn_odd_vs_even_number(number)
    fn_half_board(number)
    fn_red_vs_black(number)

import random
spin_result = random.randint(0,36)
print("The spin resulted in",spin_result)
fn_game(spin_result)
