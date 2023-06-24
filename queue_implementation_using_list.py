queue=[]
def enqueue():
    element =int(input("enter element you want to insert :"))
    queue.append(element)
    print(element,"is added to q")
def dequeue():
    if not queue:
        print("queue is empty")
    else:
        e=queue.pop(0)
        print("removed element ",e)
def display():
    print(queue)
while True:
    print("select your option: 1.add 2.delete 3.display 4.quit")
    choice=int(input())
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        display()
    elif choice==4:
        break
    else:
        print("choose correct option:")