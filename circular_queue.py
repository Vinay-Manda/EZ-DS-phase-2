class CircularQueue():
    def __init__(self,size):
        #inoitialising the queue
        self.size=size
        self.queue=[None for i in range(size)]
        self.front=self.rear=-1
    def enqueue(self,data):
        if((self.rear+1)%(self.size)==self.front):
            print("Queue overflow")
        elif(self.front==-1):
            self.front=0
            self.rear=0          
            self.queue[self.rear]=data
            print(data)
        else:
            self.rear=(self.rear+1)%self.size
            self.queue[self.rear]=data
            print(data)
    def dequeue(self):
        if(self.front==-1):
            print("queue underflow")
        elif(self.front==self.rear):
            temp=self.queue[self.front]
            self.front=-1
            self.rear=-1
            return temp
        else:
            temp=self.queue[self.front]
            self.front=(self.front+1)%self.size
            return temp
    def display(self):
        if(self.front==-1):
            print("queue underflow")
        elif(self.rear>=self.front):
            print("elements in the  circular queue are: ",end=" ")
            for i in range(self.front,self.rear+1):
                print(self.queue[i],end=" ")
                print()
        else:
            print("elements are: ",end=" ")
            for i in range(self.front,self.size):
                print(self.queue[i],end=" ")
            for i in range(0,self.rear+1):
                print(self.queue[i],end=" ")
            print()
        if((self.rear+1)%self.size==self.front):
            print("Queue is full")
ob=CircularQueue(5)
ob.enqueue(10)
ob.enqueue(12)
ob.enqueue(13)
ob.enqueue(-14)
ob.display()
print("deleted value is =",ob.dequeue())
print("deleted value is =",ob.dequeue())
ob.display()
ob.enqueue(18)
ob.enqueue(20)
ob.enqueue(15)
ob.enqueue(16)
ob.display()