
goal = [1,2,3,4,5,6,7,8,0]
start =[8,2,0,4,7,6,3,5,1]


def printPuzzle(state):
    print(' ___________\n| {} | {} | {} |\n ___________\n| {} | {} | {} |\n ___________\n| {} | {} | {} |\n -----------'.format(
        state[0],
        state[1],
        state[2],
        state[3],
        state[4],
        state[5],
        state[6],
        state[7], 
        state[8]))
    
def result(given, action):
    res = given
    idx = given.index(0)
    if(action == "up" and idx>2):
        res[idx] = given[idx-3]
        res[idx-3] = 0
    elif(action == "down" and idx<6):
        res[idx] = given[idx+3]
        res[idx+3] = 0
    elif(action == "left" and (idx%3!=0)):
        res[idx] = given[idx-1]
        res[idx-1] = 0
    elif(action == "right" and (idx%3!=2)):
        res[idx] = given[idx+1]
        res[idx+1] = 0
        
    return res
        
while(True):
    printPuzzle(start)
    
    
    print("Press 1 for up")
    print("Press 2 for down")
    print("Press 3 for left")
    print("Press 4 for right")
    ch = int(input("Enter Your Choice : "))
    
    
    
    if(ch == 1):
        start = result(start, 'up')
    elif(ch==3):
        start = result(start, 'left')
    elif(ch == 2):
        start = result(start, 'down')
    elif(ch == 4):
        start = result(start, 'right')
    
    if(goal == start ):
        print("NIce bro You have won after all....! ")
        break
                
    
    

    
    
    
