# ******************************************************************************
# * @file main.py
# * @author Pablo Joaquim
# * @brief The entry point
# *
# * @copyright NA
# *
# ******************************************************************************

# ******************************************************************************
# * import modules
# ******************************************************************************
import logging
import signal
import math

# ******************************************************************************
# * Objects Declarations
# ******************************************************************************

# ******************************************************************************
# * Object and variables Definitions
# ******************************************************************************
running = True

HEAD = 0
KNOT9 = 9
# KNOT1 = 1
# KNOT2 = 2
# KNOT3 = 3
# KNOT4 = 4
# KNOT5 = 5
# KNOT6 = 6
# KNOT7 = 7
# KNOT8 = 8
# KNOT9 = 9

# ******************************************************************************
# * Function Definitions
# ******************************************************************************

# ******************************************************************************
# * @brief Calc the length of the vector between two points
# ******************************************************************************
def calcDistance(p1, p2):
    dist = math.sqrt((p2[1]-p1[1])*(p2[1]-p1[1])+(p2[0]-p1[0])*(p2[0]-p1[0]))
    return dist

# ******************************************************************************
# * @brief Calc the length of the vector between two points
# ******************************************************************************
def processMovementRules(head, tail):
    
    #If both are in the same position do nothing
    if(head[0] == tail[0] and head[1] == tail[1]):
        return
    
    #If both are in the same row
    if(head[0] == tail[0] + 2 and head[1] == tail[1]):
        tail[0] = tail[0] + 1
        return
    
    #If both are in the same row
    if(head[0] == tail[0] - 2 and head[1] == tail[1]):
        tail[0] = tail[0] - 1
        return
    
    #If both are in the same column
    if(head[1] == tail[1] + 2 and head[0] == tail[0]):
        tail[1] = tail[1] + 1
        return
    
    #If both are in the same row
    if(head[1] == tail[1] - 2 and head[0] == tail[0]):
        tail[1] = tail[1] - 1
        return
    
    #if the head and tail aren't touching and aren't in the same row or column, the tail always moves one step diagonally to keep up
    if(head[0] != tail[0] and head[1] != tail[1]):
        if(head[0] >= tail[0] + 1):
            tail[0] = tail[0] + 1
        elif(head[0] <= tail[0] - 1):
            tail[0] = tail[0] - 1
        if(head[1] >= tail[1] + 1):
            tail[1] = tail[1] + 1 
        elif(head[1] <= tail[1] - 1):
            tail[1] = tail[1] - 1
        return   
        
    
# ******************************************************************************
# * @brief Calc the length of the vector between two points
# ******************************************************************************
def updateRopePosition(places, rope, direction, steps):
    for x in range(steps):
        if(direction == 'R'):
            rope[HEAD][0] = rope[HEAD][0] + 1
        elif(direction == 'L'):
            rope[HEAD][0] = rope[HEAD][0] - 1
        elif(direction == 'U'):
            rope[HEAD][1] = rope[HEAD][1] + 1
        elif(direction == 'D'):
            rope[HEAD][1] = rope[HEAD][1] - 1

        # print("rope:" + str(rope), flush=True)
        
        for i in range(9):
            dist = calcDistance(rope[i], rope[i+1])    
            if(dist >= 2):
                processMovementRules(rope[i], rope[i+1])
                if (i+1 == KNOT9):
                    if places.count(rope[KNOT9]) == 0:
                        places.append(list(rope[KNOT9]))
                        
    print("rope:" + str(rope), flush=True)
    
# ******************************************************************************
# * @brief The handler for the termination signal handler
# ******************************************************************************
def sigintHandler(signum, frame):
    global running
    running = False
    print('Signal handler called with signal', signum)
    raise RuntimeError("Terminating...")


# ******************************************************************************
# * @brief The main entry point
# ******************************************************************************
if __name__ == '__main__':
    signal.signal(signal.SIGINT, sigintHandler)

    # These parameters are for the werkzeug embedded web server of Flask
    # If we're using gunicorn (WSGI production web server) these parameters are not applied
    try:
        startPosition = list([0,0])
        rope = [list(startPosition), list(startPosition), list(startPosition), list(startPosition), list(startPosition), list(startPosition), list(startPosition), list(startPosition), list(startPosition), list(startPosition)]
             
        placesVisited = []
        
        # Add the initial point to the places
        placesVisited.append(list(startPosition))
        
        print("Initializing...", flush=True)

        # Open the file with the inputs
        with open('tst/input.txt') as f:
            # Move along the lines of the input file
            for line in f:
                # The separator is an EOL character
                if(line != "\n"):
                    # Remove the EOL character of every line
                    line = line.replace('\n', '')
                    values = line.split(" ")
                    direction = values[0]
                    steps = int(values[1])
                    print("direction:" + str(direction), flush=True)
                    print("steps:" + str(steps), flush=True)

                    updateRopePosition(placesVisited, rope, direction, steps)
             
                    print("route:" + str(placesVisited), flush=True)
    
            
        print("route length:" + str(len(placesVisited)), flush=True)
        
    except RuntimeError:
        print("Finishing...", flush=True)
