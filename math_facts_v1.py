import random

def get_an_integer_input_or_none():
    input_string=input()
    try:
        number=int(input_string)
    except:
        number=None
    return number

def must_get_an_integer_input():
    is_an_integer=False
    while(is_an_integer==False):
        integer_or_none=get_an_integer_input_or_none()
        if (integer_or_none is not None):
            is_an_integer=True
        else:
            print('\tNot an integer. Please try again.')
    return integer_or_none

how_many_times=50
how_many_retrys=3

right=0
for i in range(1,how_many_times+1):
    no_1=random.randint(0,10)
    no_2=random.randint(3,3)
    real_answer=no_1*no_2
    print("Question {}: {}x{}=?".format(i,no_1,no_2))
    for j in range(1,how_many_retrys+1):
        answer=must_get_an_integer_input()
        if(answer==real_answer):
            print("*^-^*correct*^-^*")
            right=right+1
            break
        else:
            if(j==how_many_retrys):
                print("\tNo it should be {}".format(real_answer))
            else:
                print("\tWrong, try again.")
print("you got {} / {}".format(right,how_many_times))
