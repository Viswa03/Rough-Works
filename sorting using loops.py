l =[6,5,9,2,4,7]


"""
l=[]
x=int(input("enter the values:"))
for k in range(0,x):
    y = int(input("enter the element of list:"))
    l.append(y)
"""
    
for i in range(0,len(l)-1):
    for j in range(i+1,len(l)):
        if (l[i] > l[j]):
            l[i],l[j] = l[j],l[i]
        print(l)
    print("shorted list:")
    print(l)
