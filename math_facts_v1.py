import random

how_many_times=50

right=0
for i in range(1,how_many_times+1):
    no_1=random.randint(0,10)
    no_2=random.randint(3,3)
    real_answer=no_1*no_2
    is_an_integer=False
    while(is_an_integer==False):
        print("Question {}: {}x{}=?".format(i,no_1,no_2))
        answer=input()
        try:
            number=int(answer)
            is_an_integer=True
        except:
            print('Not an integer. Please try again.')
    if(number==real_answer):
        print("correct")
        right=right+1
    else:
        print("No it should be {}".format(real_answer))
print("you got {} / {}".format(right,how_many_times))
