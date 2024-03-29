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
from ast import literal_eval

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
def comparePackets(input1, input2):
    order = "equal"
    
    print("- Compare ", input1, " vs ", input2)
        
    for i in range(len(input1)):
        if i<len(input2):
            #If one of the elements is a list and the other is an integer
            if(isinstance(input1[i], int) and isinstance(input2[i],list)):
                aux = [input1[i]]
                input1[i] = aux
            elif(isinstance(input1[i], list) and isinstance(input2[i],int)):
                aux = [input2[i]]
                input2[i] = aux
            
            # If both elements are integers
            if(isinstance(input1[i], int) and isinstance(input2[i],int)):
                print("  - Compare ", input1[i], " vs ", input2[i] )
                if (input1[i]<input2[i]):
                    order = "ok"
                    print("  - Left side is smaller, so inputs are in the right order")
                    break
                elif (input1[i]>input2[i]):
                    order = "nok"
                    print(" - Right side is smaller, so inputs are not in the right order")                    
                    break
                
            # If both elements are lists
            elif(isinstance(input1[i], list) and isinstance(input2[i],list)):
                order = comparePackets(input1[i], input2[i])
                if(order != "equal"):
                    break
                
        else:
            order = "nok"
            print("  - Right side ran out of items, so inputs are not in the right order")
            break
            # return order
    
    if order is "equal" and (len(input1) < len(input2) ):
        order = "ok"
        print("  - Left side ran out of items, so inputs are in the right order")
    
    return order
   
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
        packets = []
        
        print("Initializing...", flush=True)

        # Open the file with the inputs
        with open('tst/input.txt') as f:
            while (True):
                packet1 = f.readline()
                packet2 = f.readline()
                delimiter = f.readline()
                
                # Check for EOF
                if not packet1:
                    break
                if not packet2:
                    break
                if (packet1 != "\n" and packet2 != "\n"):
                    packet1 = packet1.replace('\n', '').lstrip()
                    packet2 = packet2.replace('\n', '').lstrip()
                    packets.append((literal_eval(packet1),literal_eval(packet2)))
                     
        print(packets)
        cnt = 0
        total = 0
        for x in packets:
            cnt = cnt+1
            print ("\n== Pair ", str(cnt), " ==")
            if (comparePackets(x[0], x[1]) == "ok"):
                total = total + cnt
            
        # print(literal_eval(packets[1][0]))
        print(total)
        
    except RuntimeError:
        print("Finishing...", flush=True)
