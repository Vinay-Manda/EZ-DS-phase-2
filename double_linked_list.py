#creating node-declaration & definition
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class Singlelinkedlist:
    def __init__(self):
        self.head=None

    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp=self.head#temp=first node
            while temp:
                print(temp.data,"->",end=" ")
                #temp.data means first node's data
                temp=temp.next#establishing linked list
            while temp:
                print(temp.data,"->",end=" ")
                temp=temp.prev
#     def rev_traversal(self):
#         if self.head is None:
#             print("Linked list is empty")
#         else:
#             temp=self.head
#             while temp:
#                 temp=temp.next
#             while temp:
#                 print(temp.data,"->",end=" ")
#                 temp=temp.prev
obj=Singlelinkedlist()
#node creation-initializing
n=Node(10)#so n.data in Node class will be 10
obj.head=n#assigning first node as head
n1=Node(20)
n.next=n1
n1.prev=n#next node value
n2=Node(30)
n1.next=n2
n2.prev=n1
n3=Node(40)
n2.next=n3
n3.prev=n2
n4=Node(50)
n3.next=n4
n4.prev=n3
obj.display()
#obj.rev_traversal()

