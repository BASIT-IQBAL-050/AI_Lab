import keyboard

goal = [1,2,3,4,5,6,7,8,0]
start =[8,2,0,4,7,6,3,5,1]


#printing the puzzle 
def printPuzzle(state):
    print(' ___________\n| {} | {} | {} |\n ___________\n| {} | {} | {} |\n ___________\n| {} | {} | {} |\n -----------'.format(
        state[0], state[1], state[2],
        state[3], state[4], state[5],
        state[6], state[7], state[8]))
    
# Finding the result based on actions performed
def result(Incomming, action):
    outgoing = Incomming
    index = Incomming.index(0)
    if(action == "up" and index>2):
        outgoing[index] = Incomming[index-3]
        outgoing[index-3] = 0
    elif(action == "down" and index<6):
        outgoing[index] = Incomming[index+3]
        outgoing[index+3] = 0
    elif(action == "left" and (index%3!=0)):
        outgoing[index] = Incomming[index-1]
        outgoing[index-1] = 0
    elif(action == "right" and (index%3!=2)):
        outgoing[index] = Incomming[index+1]
        outgoing[index+1] = 0
        
    return outgoing
        
        



        
# Running the Game
print("...............You Can Use Arrow Keys to Move ..........")
while(True):
    printPuzzle(start)
    print("")
    print("")
    print("")
    print("      -----      ")
    print("     |  W  |      ")
    print(" ----------------")
    print("| A  |  S  |  D  |")    
    print(" ----------------")
    
  
    ch = input("Enter Your Choice : ")
    
    if(ch  in ['W','A','S', 'D','w', 'a', 's', 'd']):
        if(ch == 'W' or ch== 'w'):
            start = result(start, 'up')
        elif(ch=='A'or ch == 'a'):
            start = result(start, 'left')
        elif(ch == 'S' or ch == 's'):
            start = result(start, 'down')
        elif(ch == 'D' or ch == 'd'):
            start = result(start, 'right')
    
    if(goal == start ):
        print("Congrats....! You have Won the GAme")
        break
                
    
    

    
    
    
