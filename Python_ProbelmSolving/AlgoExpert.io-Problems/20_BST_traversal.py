"""
 Inorder, Preorder and Postorder Traversal of a Tree
"""
class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = Tree(10)
root.left = Tree(5)
root.right = Tree(15)
root.left.left = Tree(2)
root.left.right = Tree(5)
root.left.left.left = Tree(1)
root.right.right = Tree(22)

def inOrderTraversal_recursive(root, resultArray):
    if root:
        inOrderTraversal_recursive(root.left, resultArray)
        resultArray.append(root.data)
        inOrderTraversal_recursive(root.right, resultArray)
        print(resultArray)
    
    return resultArray

def preOrderTraversal_recursive(root, resultArray):
    if root:
        resultArray.append(root.data)
        preOrderTraversal_recursive(root.left, resultArray)
        preOrderTraversal_recursive(root.right, resultArray)
        print(resultArray)
    
    return resultArray

def postOrderTraversal_recursive(root, resultArray):
    if root:
        postOrderTraversal_recursive(root.left, resultArray)
        postOrderTraversal_recursive(root.right, resultArray)
        resultArray.append(root.data)
        print(resultArray)

    return resultArray

print('*'*10)
preOrderTraversal_recursive(root, resultArray=[])
print('*'*10)
postOrderTraversal_recursive(root, resultArray=[])
print('*'*10)
inOrderTraversal_recursive(root, resultArray=[])
print('*'*10)


def inOrderTraversal_iterative(root):
    stack = []

    while True:
        if root:
            stack.append(root)
            root = root.left
        elif stack:
            root = stack.pop()
            print(root.data)
            root = root.right
        else:
            break

inOrderTraversal_iterative(root)


def preOrderTraversal_iterative(root):
    stack = []

    while True:
        if root:
            stack.append(root)
            print(root.data)
            root = root.left
        elif stack:
            root = stack.pop()
            root = root.right
        else:
            break
print('*'*10)
preOrderTraversal_iterative(root)

def postOrderTraversal_iterative(root):
    s1 = []
    s2 = []

    while s1:
            
        # Pop an item from s1 and 
        # append it to s2
        node = s1.pop()
        s2.append(node)
        
        # Push left and right children of 
        # removed item to s1
        if node.left:
            s1.append(node.left)
        if node.right:
            s1.append(node.right)

    # Print all elements of second stack
    while s2:
        node = s2.pop()
        print(node.data)

print('*'*10)
postOrderTraversal_iterative(root)