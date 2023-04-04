n=int(input("ENTER THE VALUE:"))
i=0
for i in range(n):
    if i%5==0 and i%3==0:
        print("fizzbuzz")
    if i%3==0:
        print("fizz")
    elif i%5==0:
        print("buzz")
    else:
        print(i)
        
