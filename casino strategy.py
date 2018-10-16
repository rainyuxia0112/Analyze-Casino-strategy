#solution 1
from numpy.random import choice
win_lost=[1,0]
pro=[18/37,19/37]

list=[]
for i in range(72):
     list.append(choice(win_lost,p=pro))
reverse_list=list
reverse_list.reverse()
n=reverse_list.index(1)
import math
value=-5*(1-math.pow(2,n))
s=sum(list)
sum_total=s*5-value

def total(days):
    l = []
    for m in range(days):
        from numpy.random import choice
        win_lost = [1, 0]
        pro = [18 / 37, 19 / 37]

        list = []
        for i in range(72):
            list.append(choice(win_lost, p=pro))
        reverse_list = list
        reverse_list.reverse()
        n = reverse_list.index(1)
        import math
        value = -5 * (1 - math.pow(2, n))
        s = sum(list)
        sum_total = s * 5 - value
        l.append(sum_total)
    return l



#solution 2
def choose():
     from numpy.random import choice
     win_lost=[1,0]
     pro=[18/37,19/37]
     return choice(win_lost,p=pro)


def value(v,m,p):
    if p:
        v=v+m
        return v
    else:
        v=v-m
        return v

def money(m,p):
    if p:
        return 5
    else:
        return m*2

n=1
v=0
m=5

while n<=72:
    p=choose()
    v=value(v,m,p)
    m=money(m,p)
    n+=1
print (v)
list=[]
for i in range(1000):
    n = 1
    v = 0
    m = 5
    while n <= 72:
        p = choose()
        v = value(v, m, p)
        m = money(m, p)
        n += 1
    list.append(v)




import numpy
outcome = ["red", "black", "green"]
game_prob = [18/37, 18/37, 1/37]

def play_game():
    result = numpy.random.choice(outcome, p = game_prob)
    return result

def get_output(input, result):
    if (result == "red"):
        output = input
    else:
        output = -(input)
    return output

def adjust_bet(input, result):
    if (result == "red"):
        input = 5
    else:
        input = input*2
    return input

n = 72
bet = 5
list = []
for a in range(100):
    total_earning = 0
    for i in range(n):
        result = play_game()
        delta = get_output(bet, result)
        bet = adjust_bet(bet, result)
        total_earning += delta
    bet=5
    list.append(total_earning)

average = numpy.mean(list)

