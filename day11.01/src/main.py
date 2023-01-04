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
class Monkey:
    OPERATION_SUM = '+'
    OPERATION_MULTIPLY = '*'
    OPERATION_SQUARED = '2'

    def __init__(self, items, operation, operand, testDivider, monkeyDestTestTrue, monkeyDestTestFalse):
        self.items = list(items)
        self.operation = operation
        self.operand = operand
        self.testDivider = testDivider
        self.monkeyDestTestTrue = monkeyDestTestTrue
        self.monkeyDestTestFalse = monkeyDestTestFalse
        self.monkeybusiness = 0
        print("Monkey items: " + str(self.items), flush=True)
        print("Monkey operation: " + str(self.operation), flush=True)
        print("Monkey operand: " + str(self.operand), flush=True)
        print("Monkey testDivider: " + str(self.testDivider), flush=True)
        print("Monkey monkeyDestTestTrue: " + str(self.monkeyDestTestTrue), flush=True)
        print("Monkey monkeyDestTestFalse: " + str(self.monkeyDestTestFalse), flush=True)

    def updateItems(self, items):
        self.items.append(items)
    
# ******************************************************************************
# * Object and variables Definitions
# ******************************************************************************
running = True

# ******************************************************************************
# * Function Definitions
# ******************************************************************************

    
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
        monkeys = []
        
        print("Initializing...", flush=True)

        # Open the file with the inputs
        with open('tst/input.txt') as f:
            while (True):
                line = f.readline()
                # Check for EOF
                if not line:
                    break
                if (line != "\n"):
                    line = line.replace(':\n', '').lstrip()
                    # Get the monkey index
                    values = line.split(" ")
                    monkeyIdx = int(values[1])
                    
                    # Get the monkey initial items                
                    line = f.readline().replace('\n', '').replace(',', '').lstrip()
                    values = line.split(" ")
                    items = list()
                    for x in values[2:]:
                        items.append(int(x))                    
                    
                    # Get the operation
                    line = f.readline().replace('\n', '').lstrip()
                    values = line.split(" ")
                    if (values[3] == values[5] and values[4] == '*'):
                        operation = Monkey.OPERATION_SQUARED
                        operand = 0
                    elif (values[4] == '*'):
                        operation = Monkey.OPERATION_MULTIPLY
                        operand = int(values[5])
                    else:
                        operation = Monkey.OPERATION_SUM
                        operand = int(values[5])
                    
                    # Get the test
                    line = f.readline().replace('\n', '').lstrip()
                    values = line.split(" ")
                    testDivider = int(values[3])
                    
                    # Get the True condition
                    line = f.readline().replace('\n', '').lstrip()
                    values = line.split(" ")
                    monkeyDestTestTrue = int(values[5])
                    
                    # Get the False condition
                    line = f.readline().replace('\n', '').lstrip()
                    values = line.split(" ")
                    monkeyDestTestFalse = int(values[5])
                    
                    # Create the monkey object
                    monkey = Monkey(items, operation, operand, testDivider, monkeyDestTestTrue, monkeyDestTestFalse)
                    # Add the monkey to the list
                    monkeys.insert(monkeyIdx, monkey)
    
    
        for round in range(20):
            monkeyIdx = 0
            for monkey in monkeys:
                print("-------------Monkey:" + str(monkeyIdx), flush=True)
                monkeyIdx = monkeyIdx + 1
                items = monkey.items
                monkey.items = []
                
                # Calc how many items the monkey will inspect
                monkey.monkeybusiness = monkey.monkeybusiness + len(items)
                
                # Process the rules over each item
                print("items:" + str(items), flush=True)
                for item in items:
                    worrylevel = item
                    if(monkey.operation == Monkey.OPERATION_SQUARED):
                        worrylevel = worrylevel * worrylevel
                    elif(monkey.operation == Monkey.OPERATION_MULTIPLY):
                        worrylevel = worrylevel * monkey.operand
                    else:
                        worrylevel = worrylevel + monkey.operand
                    worrylevel = int(worrylevel / 3)
                    testValue = worrylevel % monkey.testDivider                
                    if(testValue == 0):
                        monkeys[monkey.monkeyDestTestTrue].items.append(worrylevel)
                        print("worrylevel:" + str(worrylevel) + " ->Monkey: " + str(monkey.monkeyDestTestTrue), flush=True)
                    else:
                        monkeys[monkey.monkeyDestTestFalse].items.append(worrylevel)
                        print("worrylevel:" + str(worrylevel) + " ->Monkey: " + str(monkey.monkeyDestTestFalse), flush=True)

            for monkey in monkeys:
                print("Monkey items:" + str(monkey.items), flush=True)
                print("Monkeybusiness:" + str(monkey.monkeybusiness), flush=True)

        # Find the two monkeys with the largest monkeybusiness
        monkeybusinesses = []
        for monkey in monkeys:
            monkeybusinesses.append(monkey.monkeybusiness)
        monkeybusinesses.sort(reverse=True)
        print("----->monkeybusinesses:" + str(monkeybusinesses), flush=True)
        result = monkeybusinesses[0] * monkeybusinesses[1]
        print("----->result:" + str(result), flush=True)
        # print("route length:" + str(len(placesVisited)), flush=True)
        
    except RuntimeError:
        print("Finishing...", flush=True)
