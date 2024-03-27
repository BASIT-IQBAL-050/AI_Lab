
def removeDuplicate(x):
    y = []
    for i in x:
        if i not in y:
            y.append(i)
    return y


x=[1,1,2,2,2,3,3,3,3]

print(removeDuplicate(x))