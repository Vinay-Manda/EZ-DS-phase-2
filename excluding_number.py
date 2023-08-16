#print 1 to 100 excluding 9,14,99,74,84,24
l=(9,14,99,74,84,24)
l1=[]
for i in range(1,101):
    if i not in l:
        l1.append(i)
    if i in l:
        continue
print(l1)