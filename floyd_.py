class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
        def push(self,new_data):
            new_node=Node(new_data)
            new_node.next=self.head
            self.head=new_node
        def detectandremoveloop(self):
            if self.head is None:
                return
            slow_p=slow_p.next
            fast_p=fast_p.next.next
            #if slow_p and fast_p meet at same point
            if slow_p==fast_p:
                print("meeting point",slow_p.data)
                slow_p=self.head
                #finding begining of loop
                while(slow_p.next!=fast_p.next):
                    slow_p=slow_p.next
                    fast_p=fast_p.next
                    #since fast.next is looping point
                print("start of loop",fast_p.next.data)
                fast_p.next=None
        def printlist(self):
            temp=self.head
            while(temp):
                print(temp.data,end=' ')
                temp=temp.next
llist=linkedlist()
llist.head=Node(50)
llist.head.next=Node(20)
llist.head.next.next=Node(15)
llist.head.next.next.next=Node(4)
llist.head.next.next.next.next=Node(10)
extra=Node(1)
llist.head.next.next.next.next.next=extra
extra.next=llist.head.next
llist.detectandremoveloop()
print("Linked list after removing loop")
llist.printlist()