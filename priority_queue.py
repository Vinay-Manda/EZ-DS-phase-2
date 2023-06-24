stud=[]
stud.append((1,'karthik'))
stud.append((2,'sai'))
stud.append((4,'vinay'))
stud.append((3,'arjun'))
stud.sort(reverse=True)
print("priority wise")
print(stud)
print("original queue")
while stud:
    print(stud.pop())