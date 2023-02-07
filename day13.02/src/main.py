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

# ******************************************************************************
# * @brief This functions compare two packets using the proposed rules
# ******************************************************************************
def comparePackets(input1, input2):
    order = "equal"
    
    cmp1 = input1.copy()
    cmp2 = input2.copy()
    # print("- Compare ", input1, " vs ", input2)
        
    for i in range(len(cmp1)):
        if i<len(cmp2):
            #If one of the elements is a list and the other is an integer
            if(isinstance(cmp1[i], int) and isinstance(cmp2[i],list)):
                aux = [cmp1[i]]
                cmp1[i] = aux
            elif(isinstance(cmp1[i], list) and isinstance(cmp2[i],int)):
                aux = [cmp2[i]]
                cmp2[i] = aux
            
            # If both elements are integers
            if(isinstance(cmp1[i], int) and isinstance(cmp2[i],int)):
                # print("  - Compare ", input1[i], " vs ", input2[i] )
                if (cmp1[i]<cmp2[i]):
                    order = "ok"
                    # print("  - Left side is smaller, so inputs are in the right order")
                    break
                elif (cmp1[i]>cmp2[i]):
                    order = "nok"
                    # print(" - Right side is smaller, so inputs are not in the right order")                    
                    break
                
            # If both elements are lists
            elif(isinstance(cmp1[i], list) and isinstance(cmp2[i],list)):
                order = comparePackets(cmp1[i], cmp2[i])
                if(order != "equal"):
                    break
                
        else:
            order = "nok"
            # print("  - Right side ran out of items, so inputs are not in the right order")
            break
            # return order
    
    if order == "equal" and (len(cmp1) < len(cmp2) ):
        order = "ok"
        # print("  - Left side ran out of items, so inputs are in the right order")
    
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
        
        # Adding the divider packets to the input data
        divider1 = literal_eval("[[2]]")
        divider2 = literal_eval("[[6]]")
        packets.append(divider1)
        packets.append(divider2)
        
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
                    # packets.append((literal_eval(packet1),literal_eval(packet2)))
                    packets.append(literal_eval(packet1))
                    packets.append(literal_eval(packet2))
        
                     
        n = len(packets)
        for i in range(n-1):
            for j in range(n-1-i):
                if (comparePackets(packets[j], packets[j+1]) == "nok"):
                    packets[j], packets[j+1] = packets[j+1], packets[j]        
        
        print('\n'.join(map(str,packets)))
        
        cnt = 0
        div1_pos = 0
        div2_pos = 0
        for x in packets:
            cnt = cnt + 1
            if (x == divider1):
                print ("div1 found at ", cnt)
                div1_pos = cnt
            if (x == divider2):
                print ("div2 found at ", cnt)
                div2_pos = cnt
        
        print("Distress signal is ", div1_pos * div2_pos )
    
            
        
        
    except RuntimeError:
        print("Finishing...", flush=True)
