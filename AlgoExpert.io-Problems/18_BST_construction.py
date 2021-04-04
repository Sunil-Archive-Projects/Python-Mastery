"""
BST Implementation. 
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(root, newVal):
    currentNode = root

    while True:
        if newVal < currentNode.val:
            if currentNode.left is None:
                currentNode.left = Node(newVal)
                break
            else:
                currentNode = currentNode.left
        else:
            if currentNode.right is None:
                currentNode.right = Node(newVal)
                break
            else:
                currentNode = currentNode.right
                

def contains(root, searchVal):
    currentNode = root

    while currentNode:
        if searchVal > currentNode.val:
            currentNode = currentNode.right
        elif searchVal < currentNode.val:
            currentNode = currentNode.left
        else:
            return True

    return False


"""
Needs better understanding.
Do it on pen and paper first.
Refer Youtube too.
"""
def remove(root, deleteVal, parentNode=None):
    currentNode = root

    while currentNode:
        if deleteVal < currentNode.val:
            parentNode = currentNode
            currentNode = currentNode.left
        elif deleteVal > currentNode.val:
            parentNode = currentNode
            currentNode = currentNode.right
        else:
             if currentNode.left and currentNode.right:
                 #inorder successor
                 currentNode.value = currentNode.right.getMinValue()
                 currentNode.right.remove(root, currentNode.val, currentNode)




root = Node(10)
insert(root, 20)
insert(root, 30)
insert(root, 0)

print(contains(root, 10))