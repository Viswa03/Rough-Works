class sample:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        print(self.a + self.b)
    def sub(self):
        print(self.a - self.b)
    def mul(self):
        print(self.a * self.b)
    def div(self):
        print(self.a / self.b)

while True:
    opt = int(input("[1] add [2] sub [3] mul [4] div \n enter:"))
    x= int(input("enter value x:"))
    y= float(input("enter value y:"))
    res=sample(x,y)
    if opt ==1:
        res.add()
    elif opt ==2:
        res.sub()
    elif opt ==3:
        res.mul()
    elif opt ==4:
        res.div()
