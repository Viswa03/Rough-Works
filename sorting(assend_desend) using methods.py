data =[]
while True:
    opt=int(input("[1] Sequence no [2] assend [3] desend \nEnter:"))
    if opt == 1:
        n= (input("ENTER THE NUMBER:"))
        data.append(n)
        print (data)
    elif opt ==2:
        data.sort()
        print("LIST IN ASSENDING ORDER:",data)
    elif opt ==3:
        data.sort(reverse=True)
        print("LIST IN DESENDING ORDER:",data)
