import random

how_many_times=50

right=0
for i in range(1,how_many_times+1):
    no_1=random.randint(0,100)
    no_2=random.randint(0,20)
    real_answer=no_1+no_2
    print("Question {}: {}+{}=?".format(i,no_1,no_2))
    answer=input()
    number=int(answer)
    if(number==real_answer):
        print("correct")
        right=right+1
    else:
        print("no it should be {}".format(real_answer))
print("you got {} / {}".format(right,how_many_times))
