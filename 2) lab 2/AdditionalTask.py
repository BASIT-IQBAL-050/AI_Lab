from collections import deque

goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]

start =[8,2,0,4,7,6,3,5,1]
# printing the puzzle
def printPuzzle(state):
    print(' ___________')
    for i in range(3):
        print('| {} | {} | {} |'.format(state[3 * i], state[3 * i + 1], state[3 * i + 2]))
        if i < 2:
            print(' ___________')

# Finding the result based on actions performed
def result(incoming, action):
    outgoing = incoming.copy()
    index = incoming.index(0)
    if action == "up" and index > 2:
        outgoing[index], outgoing[index - 3] = outgoing[index - 3], outgoing[index]
    elif action == "down" and index < 6:
        outgoing[index], outgoing[index + 3] = outgoing[index + 3], outgoing[index]
    elif action == "left" and (index % 3 != 0):
        outgoing[index], outgoing[index - 1] = outgoing[index - 1], outgoing[index]
    elif action == "right" and (index % 3 != 2):
        outgoing[index], outgoing[index + 1] = outgoing[index + 1], outgoing[index]
    return outgoing

# Breadth-First Search Solver
def solve(start):
    queue = deque([(start, [])])
    visited = set()
    while queue:
        current, path = queue.popleft()
        if current == goal:
            return path
        visited.add(tuple(current))
        for action in ["up", "down", "left", "right"]:
            new_state = result(current, action)
            if tuple(new_state) not in visited:
                queue.append((new_state, path + [action]))
    return None

# Running the Game
print("...............You Can Use WASD Keys to Move ..........")
while True:
    printPuzzle(start)
    print("")
    print("")
    print("")
    print("      -----      ")
    print("     |  W  |      ")
    print(" ----------------")
    print("| A  |  S  |  D  |")    
    print(" ----------------")
  
    ch = input("Enter Your Choice : ").lower()
    
    if ch in ['w', 'a', 's', 'd']:
        start = result(start, ch)
        solution = solve(start)
        if solution:
            for step in solution:
                printPuzzle(start)
                print("Move:", step)
                print("")
                input("Press Enter to continue...")
                start = result(start, step)
        else:
            print("No solution found!")
            break
    else:
        print("Invalid input!")
