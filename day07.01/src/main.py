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
    
    "Inorder traversal algorithm to print the content of the tree"
    def printTree(self, lvl=0):
        if(self.attributes == "dir"):
            print(" " * lvl + "- " + str(self.name) + " (dir, size="  + str(self.size) +")", flush=True)
        else:
            print(" " * lvl + "- " + str(self.name) + " (file, size=" + str(self.size) + ")", flush=True)

        for x in self.children.values():
            current_level = lvl + 1
            x.printTree(current_level) 

    "Inorder traversal algorithm to calc the size of the sleeves of the tree"
    def calcSizes(self):
        if(self.attributes == "dir"):
            for x in self.children.values():
                self.size = self.size + x.calcSizes()
        return self.size


# ******************************************************************************
# * Object and variables Definitions
# ******************************************************************************
running = True

# ******************************************************************************
# * Function Definitions
# ******************************************************************************

def calcSizeBigDirectories (node, maxSize=0):
    sizeBigDirectories = 0
    if(node.attributes == "dir"):
        for x in node.children.values():
            if (x.attributes == "dir"):
                sizeBigDirectories = sizeBigDirectories + calcSizeBigDirectories(x, maxSize)
        if(node.size <= maxSize):
           sizeBigDirectories =  sizeBigDirectories + node.size
    return sizeBigDirectories

    


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
        with open('tst/input.txt') as f:
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
                          directory = line[5:]
                          print("Entering in directory:" + str(directory), flush=True)
                          node = node.children[directory]
                        
                        elif (line.startswith("$ ls")):
                          print("command found:" + str(line), flush=True)
        
                    else:
                        if (line.startswith("dir")):
                            dirName = line[4:]
                            nodeAux = Node(dirName, attributes="dir", parent=node)
                            node.add_child(nodeAux)
                        else:
                            fileInfo = line.split(" ")
                            nodeAux = Node(fileInfo[1], attributes="file", size=int(fileInfo[0]), parent=node)
                            node.add_child(nodeAux)
        
        root.calcSizes()
        root.printTree()
        size = calcSizeBigDirectories(root, 100000)
        print("Max Directory Size:" + str(size), flush=True)
        
    except RuntimeError:
        print("Finishing...", flush=True)
