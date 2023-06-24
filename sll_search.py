#creating node-declaration & definition
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
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
    def search(self,sear):
        temp=self.head
        flag=0
        while temp:
            if temp.data==sear:
                print("data is present",temp.data)
                flag=1
                break
            if flag==0:
                print("data not found")
                break
obj=Singlelinkedlist()
#node creation-initializing
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
obj.display()
print()
obj.search(10)

