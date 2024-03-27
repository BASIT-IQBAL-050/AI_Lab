import random 

ranNum = random.randint(1,100)


sumOfLess=0
sumOfGreat=0
print(ranNum)

for i in range(ranNum-1, ranNum-11, -1):
   sumOfLess+=i
  

for i in range(ranNum+1, ranNum+11):
  sumOfGreat+=i

print("Sum of Previous 10 Num then ", ranNum, " are ", sumOfLess)
print("Sum of Greater 10 Num then ", ranNum, " are ", sumOfGreat)

