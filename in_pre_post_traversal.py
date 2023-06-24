class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
def printinorder(root):
    if root:
        printinorder(root.left)
        print(root.val,end=" ")
        printinorder(root.right)
def printpostorder(root):
    if root:
        printinorder(root.left)
        printinorder(root.right)
        print(root.val,end=" ")
def printpreorder(root):
    if root:
        print(root.val,end=" ")
        printinorder(root.left)
        printpostorder(root.right)
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
print("Pre order")
printpreorder(root)
print()
print("Post order")
printpostorder(root)
print()
print("in order")
printinorder(root)