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
    def insert_begin(self):
        n=Node(5)
        temp=n
        temp.next=self.head
        self.head.prev=temp
        self.head=temp
    def insert_end(self):
        n=Node(60)
        temp=self.head
        while temp.next!=None:
            temp=temp.next
        temp.next=n
        n.prev=temp
    def insert_pos(self,pos):
        n=Node(15)
        temp=self.head
        for i in range(1,pos-1):
            temp=temp.next
        n.prev=temp
        n.next=temp.next
        temp.next.prev=n
        temp.next=n
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
print()
obj.insert_begin()
obj.display()
print()
obj.insert_end()
obj.display()
print()
obj.insert_pos(3)
obj.display()