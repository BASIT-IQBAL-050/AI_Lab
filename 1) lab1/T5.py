import random

ranNum = random.randint(1,100)

def even(n):
    if(n%2==0):
        return 'EVEN'
    else:
        return 'ODD'
    
isEven = even(ranNum)
print("Random Number generated is ", ranNum, " and it is ", isEven)