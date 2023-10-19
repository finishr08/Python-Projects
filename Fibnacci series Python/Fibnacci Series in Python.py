##Mustafa Ahmed
##BSSE-08
##Task no.1(Fibnacci series)

##==============================================================================

while True:
    a=input("write 'y' to continue and 'n' to stop.")
    if a=="n":
        break
    if a=="y":
        print("Program is automate Just enter some number")
        n=int(input("Enter Number: "))
        x=0
        y=1
        if n<=0:
            print("You have entered invalid number")
        else:
            while (x<=n):
                print(x)
                z=x+y
                x,y=y,z

