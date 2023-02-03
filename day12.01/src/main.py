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
    
def make_step(k, sourceMap, resultMap):
    for i in range(len(resultMap)):
        for j in range(len(resultMap[i])):
            if resultMap[i][j] == k:
                if i>0 and (resultMap[i-1][j]) == 0 and int(sourceMap[i-1][j]) == 0:
                    resultMap[i-1][j] = k + 1
                if j>0 and (resultMap[i][j-1]) == 0 and int(sourceMap[i][j-1]) == 0:
                    resultMap[i][j-1] = k + 1
                if i<len(resultMap)-1 and (resultMap[i+1][j]) == 0 and int(sourceMap[i+1][j]) == 0:
                    resultMap[i+1][j] = k + 1
                if j<len(resultMap[i])-1 and (resultMap[i][j+1]) == 0 and int(sourceMap[i][j+1]) == 0:
                    resultMap[i][j+1] = k + 1

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
# * @brief Helper function to print a matrix nicely
# ******************************************************************************
def printMatrix (matrix):
    for i in matrix:
        print('\t'.join(map(str, i)))
            
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
        heightmap = []
        possiblePaths = []
        
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
                    print("heights:" + str(heights), flush=True)
                    heightmap.append(heights)
    
        # Look for the Starting position
        start = 0
        for rowIdx,row in enumerate(heightmap):
            for colIdx,elems in enumerate(row):
                if (elems == 'S'):
                    start = (rowIdx, colIdx)
                    break
            if(start != 0):
                break
        
        # Look for the Starting position
        end = 0
        for rowIdx,row in enumerate(heightmap):
            for colIdx,elems in enumerate(row):
                if (elems == 'E'):
                    end = (rowIdx, colIdx)
                    break
            if(end != 0):
                break
    
        # print(start, end)
        totalRows = len(heightmap)
        totalCols = len(heightmap[0])

        # Prepare the map for the possible paths
        # Prepare a matrix with the same size of the original but filled with zeroes
        possiblePaths = [ [0] * totalRows for _ in range(totalCols)]
        # Mark the starting point with a value of 1
        possiblePaths[start[0]][start[1]] = 1
        
        print("heights")
        printMatrix(heightmap)
        
        heightmap[start[0]][start[1]] = 1
        heightmap[end[0]][end[1]] = 0
        k = 0
        while possiblePaths[end[0]][end[1]] == 0:
            k += 1
            make_step(k, heightmap, possiblePaths)
    
        # print("paths")
        # printMatrix(possiblePaths)

        thePath = getResultPath(end, possiblePaths)
        print(thePath)

        # # Move through the heighmap looking for a path
        # possiblePaths.append(start)
        # # end = False
        # # while(end == False):
        # cnt=3
        # while(cnt):
        #     for x in possiblePaths:
        #         print(possiblePaths)
        #         positions = findNextPosition(x, heightmap)
        #         possiblePaths.append(positions)
        #         # print(positions)
        #     cnt -= 1
        #     # for x in positions:
        #     #     aux = [start, x]
        #     #     possiblePaths.append(aux)
            
        #     #     positions = findNextPosition(x, heightmap)

        
    
        # for rowIdx in heightmap.__len__:
        #     for elems in row:
        #         if(elems is 'S'):
        #             break
    
        # for round in range(20):
        #     monkeyIdx = 0
        #     for monkey in monkeys:
        #         print("-------------Monkey:" + str(monkeyIdx), flush=True)
        #         monkeyIdx = monkeyIdx + 1
        #         items = monkey.items
        #         monkey.items = []
                
        #         # Calc how many items the monkey will inspect
        #         monkey.monkeybusiness = monkey.monkeybusiness + len(items)
                
        #         # Process the rules over each item
        #         print("items:" + str(items), flush=True)
        #         for item in items:
        #             worrylevel = item
        #             if(monkey.operation == Monkey.OPERATION_SQUARED):
        #                 worrylevel = worrylevel * worrylevel
        #             elif(monkey.operation == Monkey.OPERATION_MULTIPLY):
        #                 worrylevel = worrylevel * monkey.operand
        #             else:
        #                 worrylevel = worrylevel + monkey.operand
        #             worrylevel = int(worrylevel / 3)
        #             testValue = worrylevel % monkey.testDivider                
        #             if(testValue == 0):
        #                 monkeys[monkey.monkeyDestTestTrue].items.append(worrylevel)
        #                 print("worrylevel:" + str(worrylevel) + " ->Monkey: " + str(monkey.monkeyDestTestTrue), flush=True)
        #             else:
        #                 monkeys[monkey.monkeyDestTestFalse].items.append(worrylevel)
        #                 print("worrylevel:" + str(worrylevel) + " ->Monkey: " + str(monkey.monkeyDestTestFalse), flush=True)

        #     for monkey in monkeys:
        #         print("Monkey items:" + str(monkey.items), flush=True)
        #         print("Monkeybusiness:" + str(monkey.monkeybusiness), flush=True)

        # # Find the two monkeys with the largest monkeybusiness
        # monkeybusinesses = []
        # for monkey in monkeys:
        #     monkeybusinesses.append(monkey.monkeybusiness)
        # monkeybusinesses.sort(reverse=True)
        # print("----->monkeybusinesses:" + str(monkeybusinesses), flush=True)
        # result = monkeybusinesses[0] * monkeybusinesses[1]
        # print("----->result:" + str(result), flush=True)
        # print("possiblePaths:" + str(possiblePaths), flush=True)
    
    except RuntimeError:
        print("Finishing...", flush=True)
