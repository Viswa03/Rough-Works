def sort(l):
    for i in range(len(l)-1,0,-1):
        for j in range(i):
            if l[j]>l[j+1]:
                temp = l[j]
                l[j] = l[j+1]
                l[j+1]= temp


l=[]
x=int(input("enter the values:"))
for k in range(0,x):
    y = int(input("enter the element of list:"))
    l.append(y)
sort(l)

print(l)
