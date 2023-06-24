class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class stack:
    def __init__(self):
        self.head=None
    def push(self,data):
        if self.head is None:
            self.head=node(data)
        else:
            newnode=node(data)
            newnode.next=self.head
            self.head=newnode
    def pop(self):
        if self.head is none:
            print("stack underflow")
        else:
            popped=self.head.data
            self.head=self.head.next
            return popped
obj_stack=stack()
while True:
fron    print("1.Push")
    print("2.pop")
    print("3.quit")
    do=input("what would you like to do").split()
    print("do",do)
    print("do[0]",do[0])
    operation=do.strip().lower()
    if operation=="push":
        obj_stack.push(int(do[1]))
    elif operation=="pop"
    