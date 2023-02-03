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
import signal

# ******************************************************************************
# * Objects Declarations
# ******************************************************************************
    
# ******************************************************************************
# * Object and variables Definitions
# ******************************************************************************
running = True

# ******************************************************************************
# * Function Definitions
# ******************************************************************************
# ******************************************************************************
# * @brief Helper function to print a matrix nicely
# ******************************************************************************
def printMatrix (title, matrix):
    print(title)
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in matrix]))
    
    # for i in matrix:
        # print(''.join(map(str, i)))
        
# ******************************************************************************
# * @brief During each step, you can move exactly one square up, down, left, or 
# * right. To avoid needing to get out your climbing gear, the elevation of the 
# * destination square can be at most one higher than the elevation of your current 
# * square; that is, if your current elevation is m, you could step to elevation n, 
# * but not to elevation o. (This also means that the elevation of the destination 
# * square can be much lower than the elevation of your current square.)
# ******************************************************************************
def findNextPosition (currPosition, heightmap):
    
    nextPositions = []
    row = currPosition[0]
    column = currPosition[1]
    currHeight = heightmap[row][column]
    if (currHeight == 'S'):
        currHeight = 'a'

    if ((row+1)<len(heightmap)):
        # print (heightmap[row+1][column])    
        if (ord(heightmap[row+1][column]) <= ord(currHeight)+1):
            nextPositions.append((row+1,column))

    if (row>=1):
        # print (heightmap[row-1][column])
        if (ord(heightmap[row-1][column]) <= ord(currHeight)+1):
            nextPositions.append((row-1,column))


    if ((column+1)<len(heightmap[row])):
        # print (heightmap[row][column+1])
        if (ord(heightmap[row][column+1]) <= ord(currHeight)+1):
            nextPositions.append((row,column+1))

    if (column>=1):
        # print (heightmap[row][column-1])
        if (ord(heightmap[row][column-1]) <= ord(currHeight)+1):
            nextPositions.append((row,column-1))

    # print(nextPositions)
    return nextPositions

# ******************************************************************************
# * @brief During each step, you can move exactly one square up, down, left, or 
# * right. To avoid needing to get out your climbing gear, the elevation of the 
# * destination square can be at most one higher than the elevation of your current 
# * square; that is, if your current elevation is m, you could step to elevation n, 
# * but not to elevation o. (This also means that the elevation of the destination 
# * square can be much lower than the elevation of your current square.)
# * 
# * This function takes the step number k as an argument. What it does is pretty simple:
# * Scan the matrix with a double for-loop.
# * If we find a number that corresponds to the step number k , look at surrounding cells, and check if:
# * 1. There is no number yet
# * 2. The surrounding cell level is lower or at most one higer
# * And set the k+1 to that cells.
# ******************************************************************************
def make_step_in_multilevel(k, sourceMap, resultMap):
    for row in range(len(resultMap)):
        for column in range(len(resultMap[row])):
            if resultMap[row][column] == k:
                # Get the current level
                currLvl = int(sourceMap[row][column])
                
                if row>0:
                    if (resultMap[row-1][column]) == 0:
                        if (int(sourceMap[row-1][column]) <= currLvl+1):
                            resultMap[row-1][column] = k + 1
                        
                if column>0:
                    if (resultMap[row][column-1]) == 0:
                        if (int(sourceMap[row][column-1]) <= currLvl+1):
                            resultMap[row][column-1] = k + 1
                        
                if row<len(resultMap)-1:
                    if (resultMap[row+1][column]) == 0:
                        if (int(sourceMap[row+1][column]) <= currLvl+1):
                            resultMap[row+1][column] = k + 1
                        
                if column<len(resultMap[row])-1:
                    if (resultMap[row][column+1]) == 0:
                        if (int(sourceMap[row][column+1]) <= currLvl+1):
                            resultMap[row][column+1] = k + 1
                            
# ******************************************************************************
# * @brief This function takes the step number k as an argument. What it does is pretty simple:
# * Scan the matrix with a double for-loop.
# * If we find a number that corresponds to the step number k , look at surrounding cells, and check if:
# * 1. There is no number yet
# * 2. There is no wall
# * And set the k+1 to that cells.
# ******************************************************************************
def make_step_in_corridor(k, sourceMap, resultMap):
    for row in range(len(resultMap)):
        for column in range(len(resultMap[row])):
            if resultMap[row][column] == k:
                if row>0:
                    if (resultMap[row-1][column]) == 0:
                        if int(sourceMap[row-1][column]) == 0:
                            resultMap[row-1][column] = k + 1
                        
                if column>0:
                    if (resultMap[row][column-1]) == 0:
                        if int(sourceMap[row][column-1]) == 0:
                            resultMap[row][column-1] = k + 1
                        
                if row<len(resultMap)-1:
                    if (resultMap[row+1][column]) == 0:
                        if int(sourceMap[row+1][column]) == 0:
                            resultMap[row+1][column] = k + 1
                        
                if column<len(resultMap[row])-1:
                    if (resultMap[row][column+1]) == 0:
                        if int(sourceMap[row][column+1]) == 0:
                            resultMap[row][column+1] = k + 1

# ******************************************************************************
# * @brief This function find the shortest path based on this matrix.
# * This is done as follows:
# * Go to the ending point, say, the number there is k
# * Find a neighbor cell with a value k-1 , go there, decrease k by one
# * Repeat the previous step until we get to the starting point, i.e., k=1
# ******************************************************************************
def getResultPath(endPoint, resultMap):
    i, j = endPoint
    k = resultMap[i][j]
    the_path = [(i,j)]
    while k > 1:
        if i > 0 and resultMap[i - 1][j] == k-1:
            i, j = i-1, j
            the_path.append((i, j))
            k-=1
        elif j > 0 and resultMap[i][j - 1] == k-1:
            i, j = i, j-1
            the_path.append((i, j))
            k-=1
        elif i < len(resultMap) - 1 and resultMap[i + 1][j] == k-1:
            i, j = i+1, j
            the_path.append((i, j))
            k-=1
        elif j < len(resultMap[i]) - 1 and resultMap[i][j + 1] == k-1:
            i, j = i, j+1
            the_path.append((i, j))
            k -= 1
    return the_path

# ******************************************************************************
# * @brief Find the shortest path
# ******************************************************************************
def findShortestPath (mazemap, start, end, startValue, endValue):
    # Make a copy to do not modify the original map
    maze = mazemap
    
    # Prepare the map for the possible paths
    # Prepare a matrix with the same size of the original but filled with zeroes
    totalRows = len(maze)
    totalCols = len(maze[0])
    possiblePaths = [ [0] * totalCols for _ in range(totalRows)]
    # Mark the starting point with a value of 1
    possiblePaths[start[0]][start[1]] = 1
    
    printMatrix("Path", possiblePaths)

    # Move towards the maze several times from the Start till find the Exit
    maze[start[0]][start[1]] = startValue
    maze[end[0]][end[1]] = endValue
    k = 0
    while possiblePaths[end[0]][end[1]] == 0:
        k += 1
        make_step_in_multilevel(k, mazemap, possiblePaths)
    printMatrix("Path", possiblePaths)
    
    thePath = getResultPath(end, possiblePaths)
    print(thePath)
    return thePath
   
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
        mazemap = []
        
        print("Initializing...", flush=True)

        # Open the file with the inputs
        with open('tst/tst_input.txt') as f:
            while (True):
                line = f.readline()
                # Check for EOF
                if not line:
                    break
                if (line != "\n"):
                    line = line.replace('\n', '').lstrip()
                    heights = []
                    heights[:0] = line
                    # heights = [ord(x) for x in line]
                    print("heights:" + str(heights), flush=True)
                    mazemap.append(heights)
        printMatrix("Maze", mazemap)
        
        # Look for all the Starting positions
        start = []
        for rowIdx,row in enumerate(mazemap):
            for colIdx,elems in enumerate(row):
                if (elems == 'S') or (elems == 'a'):
                    start.append((rowIdx, colIdx))
        
        # Look for the Ending position
        end = 0
        for rowIdx,row in enumerate(mazemap):
            for colIdx,elems in enumerate(row):
                if (elems == 'E'):
                    end = (rowIdx, colIdx)
                    break
            if(end != 0):
                break
        
        
        # # The input file is made by characters, so I change it by numbers
        # new_mazemap = []
        # for row in mazemap:
        #     conv = [ord(x) for x in row]
        #     new_mazemap.append(conv)
        # printMatrix("new_mazemap", new_mazemap)
        
        # # Now find the path
        # path = findShortestPath(new_mazemap, start, end, ord('a'), ord('z'))
        # print(len(path)-1)
        
    except RuntimeError:
        print("Finishing...", flush=True)
