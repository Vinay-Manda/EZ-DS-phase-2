colours=("black","red","blue","pink")
shapes=("spack","club","heart","diamond")
numbers=("1","2","3","4")
print("welcome to lucky draw")
c1=str(input("enter colour you want: "))
# s1=str(input("enter shape you want: "))
# n1=str(input("enter number you want: "))
if c1=='black':
    print("you have choosen a corect value")
    s1=str(input("enter shape you want: "))
    if s1=="spack" :
        print("you are one step away from winning lottery")
        n1=str(input("enter number you want: "))
        if n1=="1":
            print("you won lucky draw")
        else:
            print("you have choose wrong number")
            print("better luck next time")
    else:
        print("you have choosen wrong shape")
        print("better luck next time")
else:
    print("better luck next time")