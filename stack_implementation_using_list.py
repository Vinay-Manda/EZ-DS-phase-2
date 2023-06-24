stack=[]
def push():
    element=int(input("Enter the element :"))
    stack.append(element)
    print(stack)
def pop():
    if not stack:
        print("stack underflow")
    else:
        e=stack.pop()
        print("The deleted element is :",e)
        print(stack)
def display():
    print("The stack elements are:",end=" ")
    print(stack)
def peek():
    if not stack:
        print("stack is empty:")
    else:
        e=stack.pop()
        print("the top of stack is :",e)
        stack.append(e)
        print(stack)
while True:
    print("Select your option 1.push 2.pop 3.display 4.peek 5.exit:",end=" ")
    choice=int(input())
    if choice==1:
        push()
    elif choice==2:
        pop()
    elif choice==3:
        display()
    elif choice==4:
        peek()
    elif choice==5:
        break
    else:
        print("enter option 1 or 2 or 3 or 4 or 5")