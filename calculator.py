class calc():
    def __init__(self):
        print("Welcome to the calculator")
        self.sum=0

    def add(self):
            try:
                a=input("Enter the value or AC or exit:")
                if(a=="AC"):
                    self.sum=0
                    print("All clear")
                elif(a=="exit"):
                    print("Thanks for using")
                else:
                    num=int(a)
                    self.sum=self.sum+num
                    print("The sum is",self.sum)
            except Exception:
                print("something wrong. Please try again")

    def sub(self):
        try:
            a=input("Enter the value or AC or exit:")
            if(a=="AC"):
                self.sum=0
                print("All clear")
            elif(a=="exit"):
                print("Thanks for using")
            else:
                num=int(a)
                if(self.sum==0):
                    self.sum=num
                    b=int(input("Enter the next value: "))
                    self.sum=self.sum-b
                    print("The value is",self.sum)
                else:
                    self.sum=self.sum-num
                    print("The value is",self.sum)
        except Exception:
            print("something wrong. Please try again")

    def mult(self):
        try:
            a=input("Enter the value or AC or exit:")
            if(a=="AC"):
                self.sum=0
                print("All clear")
            elif(a=="exit"):
                print("Thanks for using")
            else:
                num=int(a)
                if(self.sum==0):
                    self.sum=num
                    b=int(input("Enter the next value: "))
                    self.sum=self.sum*b
                    print("The value is",self.sum)
                else:
                    self.sum=self.sum*num
                    print("The value is",self.sum)
        except Exception:
            print("something wrong. Please try again")

    def div(self):
       try:
            a=input("Enter the value or AC or exit:")
            if(a=="AC"):
                self.sum=0
                print("All clear")
            elif(a=="exit"):
                print("Thanks for using")
            else:
                num=int(a)
                if(self.sum==0):
                    self.sum=num
                    b=int(input("Enter the next value: "))
                    self.sum=self.sum/b
                    print("The value is",self.sum)
                else:
                    self.sum=self.sum/num
                    print("The value is",self.sum)
       except Exception:
                print("something wrong. Please try again")

user=calc()
s=set()
try:
    n=int(input("Enter the value: "))
    user.sum=n
    s.add(n)
except Exception:
    print("Some error occured. Please try again")
if(len(s)==1):
    while True:
            f=input("Select the funtion (+,-,*,/) or AC for clear and exit to close\n")
            if(f=="+"):
                user.add()
            elif(f=="-"):
                user.sub()
            elif(f=="*"):
                user.mult()
            elif(f=="/"):
                user.div()
            elif(f=="AC"):
                user.sum=0
                print("All clear")
            elif(f=="exit"):
                break
            else:
                print("Please try again")


