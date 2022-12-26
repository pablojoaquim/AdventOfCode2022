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
from anytree import Node, RenderTree

# ******************************************************************************
# * Objects Declarations
# ******************************************************************************

class Node(object):
    
    def __init__ (self, name="root", children=None, size=0, attributes="dir", parent = None):
        self.name = name
        self.children = {}
        self.size = size
        self.attributes=attributes
        self.parent = parent
        
        if children is not None:
            for child in children:
                self.add_child(child)

    def __repr__(self):
        return self.name
    
    def add_child(self, node):
        assert isinstance(node, Node)
        self.children[node.name] = node

    def set_attr(self, attributes):
        self.attributes = attributes
    
    def set_size(self, size):
        self.size = size
    
    def set_parent(self, parent):
        assert isinstance(parent, Node)
        self.parent = parent

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
        root = Node(name = "root", attributes = "dir")
        node = Node()
        
        print("Initializing...", flush=True)

        # Open the file with the inputs
        with open('tst/tst_input.txt') as f:
            # Move along the lines of the input file
            for line in f:
                # The separator is an EOL character
                if(line != "\n"):
                    # Remove the EOL character of every line
                    line = line.replace('\n', '')
                    
                    # Check if is a command
                    if (line[0] == '$'):
                        if (line.startswith("$ cd /")):
                          print("command found:" + str(line), flush=True)
                          node = root
                        elif (line.startswith("$ cd ..")):
                          print("command found:" + str(line), flush=True)
                          if(node.parent is None):
                              node = root
                          else:
                              node = node.parent
                        
                        elif (line.startswith("$ cd ")):
                          print("command found:" + str(line), flush=True)
                          node = node.children["pepe"]
                        
                        elif (line.startswith("$ ls")):
                          print("command found:" + str(line), flush=True)
                          child = Node("pepe", attributes="dir", parent=root)
                          node.add_child(child)          
            
        # print("The tree:" + str(tree), flush=True)
        print("The tree:" + str(root), flush=True)
        
    except RuntimeError:
        print("Finishing...", flush=True)
