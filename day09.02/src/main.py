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
KNOT1 = 1
KNOT2 = 2
KNOT3 = 3
KNOT4 = 4
KNOT5 = 5
KNOT6 = 6
KNOT7 = 7
KNOT8 = 8
KNOT9 = 9

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
        # print("no estan en la misma:" + str(tail), flush=True)            
        return   
        
    
# ******************************************************************************
# * @brief Calc the length of the vector between two points
# ******************************************************************************
def updateRopePosition(places, rope, direction, steps):
    for x in range(steps):
        # prevRope = []        
        # for i in range(len(rope)):
        #     prevRope.append(list(rope[i]))
        if(direction == 'R'):
            rope[HEAD][0] = rope[HEAD][0] + 1
        elif(direction == 'L'):
            rope[HEAD][0] = rope[HEAD][0] - 1
        elif(direction == 'U'):
            rope[HEAD][1] = rope[HEAD][1] + 1
        elif(direction == 'D'):
            rope[HEAD][1] = rope[HEAD][1] - 1

        # print("prevRope:" + str(prevRope), flush=True)
        print("rope:" + str(rope), flush=True)
                
        dist = calcDistance(rope[HEAD], rope[KNOT1])
        if(dist >= 2):
            processMovementRules(rope[HEAD], rope[KNOT1])
            
            # rope[KNOT1][0] = prevRope[HEAD][0]
            # rope[KNOT1][1] = prevRope[HEAD][1]
        # print("1 dist:" + str(dist), flush=True)
        # print("1 rope:" + str(rope), flush=True)
        
        dist = calcDistance(rope[KNOT1], rope[KNOT2])
        if(dist >= 2):
            processMovementRules(rope[KNOT1], rope[KNOT2])
            # rope[KNOT2][0] = prevRope[KNOT1][0]
            # rope[KNOT2][1] = prevRope[KNOT1][1]    
        # print("2 dist:" + str(dist), flush=True)
        # print("2 rope:" + str(rope), flush=True)
        
        dist = calcDistance(rope[KNOT2], rope[KNOT3])
        if(dist >= 2):
            processMovementRules(rope[KNOT2], rope[KNOT3])
            # rope[KNOT3][0] = prevRope[KNOT2][0]
            # rope[KNOT3][1] = prevRope[KNOT2][1]  
        # print("3 dist:" + str(dist), flush=True)
        # print("3 rope:" + str(rope), flush=True)
        
        dist = calcDistance(rope[KNOT3], rope[KNOT4])
        if(dist >= 2):
            processMovementRules(rope[KNOT3], rope[KNOT4])
            # rope[KNOT4][0] = prevRope[KNOT3][0]
            # rope[KNOT4][1] = prevRope[KNOT3][1]
        # print("4 dist:" + str(dist), flush=True)
        # print("4 rope:" + str(rope), flush=True)
        
        dist = calcDistance(rope[KNOT4], rope[KNOT5])
        if(dist >= 2):
            processMovementRules(rope[KNOT4], rope[KNOT5])
            # rope[KNOT5][0] = prevRope[KNOT4][0]
            # rope[KNOT5][1] = prevRope[KNOT4][1]    
        # print("5 dist:" + str(dist), flush=True)
        # print("5 rope:" + str(rope), flush=True)
        
        dist = calcDistance(rope[KNOT5], rope[KNOT6])
        if(dist >= 2):
            processMovementRules(rope[KNOT5], rope[KNOT6])
            # rope[KNOT6][0] = prevRope[KNOT5][0]
            # rope[KNOT6][1] = prevRope[KNOT5][1]  
        # print("6 dist:" + str(dist), flush=True)
        # print("6 rope:" + str(rope), flush=True)
        
        dist = calcDistance(rope[KNOT6], rope[KNOT7])
        if(dist >= 2):
            processMovementRules(rope[KNOT6], rope[KNOT7])
            # rope[KNOT7][0] = prevRope[KNOT6][0]
            # rope[KNOT7][1] = prevRope[KNOT6][1]
        # print("7 dist:" + str(dist), flush=True)
        # print("7 rope:" + str(rope), flush=True)
        
        dist = calcDistance(rope[KNOT7], rope[KNOT8])
        if(dist >= 2):
            processMovementRules(rope[KNOT7], rope[KNOT8])
            # rope[KNOT8][0] = prevRope[KNOT7][0]
            # rope[KNOT8][1] = prevRope[KNOT7][1]    
        # print("8 dist:" + str(dist), flush=True)
        # print("8 rope:" + str(rope), flush=True)
        
        dist = calcDistance(rope[KNOT8], rope[KNOT9])
        if(dist >= 2):
            processMovementRules(rope[KNOT8], rope[KNOT9])
            # rope[KNOT9][0] = prevRope[KNOT8][0]
            # rope[KNOT9][1] = prevRope[KNOT8][1]                         
            if (places != None):
                if places.count(rope[KNOT9]) == 0:
                    places.append(list(rope[KNOT9]))
        # print("9 dist:" + str(dist), flush=True)
        # print("9 rope:" + str(rope), flush=True)
        
        # print("headPosition:" + str(head), flush=True)
        # print("tailPosition:" + str(rope[KNOT9]), flush=True)      

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
                    
                    
                    # print("headPosition:" + str(headPosition), flush=True)
                    # print("tailPosition:" + str(tailPosition), flush=True)               
                    print("route:" + str(placesVisited), flush=True)
    
            
        print("route length:" + str(len(placesVisited)), flush=True)
        
             
        
        
    except RuntimeError:
        print("Finishing...", flush=True)
