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
        printpostorder(root.left)
        printpostorder(root.right)
        print(root.val,end=" ")
def printpreorder(root):
    if root:
        print(root.val,end=" ")
        printpreorder(root.left)
        printpreorder(root.right)
root=Node(10)
root.left=Node(20)
root.right=Node(30)
root.left.left=Node(40)
root.left.right=Node(50)
root.right.left=Node(60)
root.right.right=Node(70)
root.left.left.left=Node(80)
root.left.left.right=Node(90)
root.left.right.left=Node(100)
root.left.right.right=Node(110)
root.right.left.left=Node(120)
root.right.left.right=Node(130)
root.right.right.left=Node(140)
root.right.right.right=Node(150)
print("Pre order")
printpreorder(root)
print()
print("Post order")
printpostorder(root)
print()
print("in order")
printinorder(root)
