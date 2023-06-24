class Node:
    def _init_(self,data):
        self.data=data
        self.next=None
class SLL:
    def _init_(self):
        self.head=None
    def singlelinkedlist:
        def _init_(self):
            self.head=None
    def insert_beginning(self,data):
        nb=Node(data)
        nb.next=self.head
        self.head=nb
        
    def insert_end(self,data):
        ne=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=ne
        ne.next=None
        
        
    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp=self.head #temp=first node
            while temp:
                if temp.next is not None:
                    print(temp.data,"->",end=' ')
                else:
                    print(temp.data,end=' ') #temp.data means first node's data
                temp=temp.next#establishing link
                
                
obj=SLL()
#node creation_initialising
n=Node(10)#so n.data in Node class will be 10
obj.head=n   #assigning first node as head
n1=Node(20)
n.next=n1 #next node value
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
n4=Node(50)
n3.next=n4
n5=Node(60)
n4.next=n5
print("before inserting 100")
obj.display()
print(" ")
print("after inserting 100 at begin")
obj.insert_beginning(100)
obj.display() #traverse
print(" ")
print("after inserting 555 at bagin")
obj.insert_beginning(555)
obj.display()
print(" ")
print("after inserting 100 at end")
obj.insert_end(100)
obj.display()