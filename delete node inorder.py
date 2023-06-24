'''logic
1.using "insert" create bst
2.input node to bee deleted
3.spot or find the node which u want to delete
(search)
4.once u find the node,
check it comes under which category of delete
5.apply the delete concept
6.find the in order succesor using separate function to replace with node to be deleted'''
class Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key,end=" ",)
        inorder(root.right)
def insert(node,key):
    if node is None:
        return Node(key)
    if key<node.key:
        node.left=insert(node.left,key)
    else:
        node.right=insert(node.right,key)
    return node
#given  a non empty binary
#search tree,return th node
#with minum key value
#found in that tree.note that the
#entire tree does not need to be searched
def minValueNode(node): #right sub tree
    current=node
    #loop down to find the left most leaf
    while(current.left is not None):
        current=current.left
    return current
#given a binary search tree and a key,this function
#delete the key and returns thenew root
def deleteNode(root,key):
    if root is None:
        return root
    #key<root,it lies in left subtree
    if key<root.key:
        root.left=deleteNode(root.left,key)
    elif(key>root.key):
        root.right=deleteNode(root.right,key)
    #if key is same as root's key
    #to b deleted
    else:
        #node with only one child or no child
        if root.left is None:
            temp=root.right
            root=None
            return temp
        elif root.right is None:
            temp=root.left
            root=None
            return temp
        #Node with two children:
        #get the inorder succesor
        #(smaallest in the right subtree)
        temp=minValueNode(root.right)
        root.key=temp.key
        root.right=deleteNode(root.right,temp.key)
    return root
root=None
root=insert(root,50)
root=insert(root,30)
root=insert(root,20)
root=insert(root,40)
root=insert(root,70)
root=insert(root,60)
root=insert(root,80)
print("Inorder:")
inorder(root)
print("\nDelete 20")
root=deleteNode(root,20)
print("Inorder:modified tree")
inorder(root)
print("\nDelete 30")
root=deleteNode(root,30)
print("inorder:modified tree")
inorder(root)
print("\nDelete 50")
root=deleteNode(root,50)
print("Inorder:modified tree")
inorder(root)