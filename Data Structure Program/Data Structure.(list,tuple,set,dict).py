while True:
    a=input("Write “y” if you want to Continue...\nWrite “n” if you don’t want to Continue...\nEnter: ")
    if a=="n":
        print()
        print("Data Structure Program is Exit")
        break
    if a=="y":
        b=input("For List write “l”\nFor tuple write “t”\nFor dictionary write “d”\nFor set write “s”\nEnter: ")
    elif a!="y" and a!="n":
        print("Plz Enter either y or n")
        b=(input("Write “y” if you want to Continue or Write “n” if you don’t want to Continue"))
    if b=="l":
        c=int(input("Enter number for list :"))
        d=[]
        for i in range(c):
            x=int(input("Enter number :"))
            d.append(x)
        print(d)
        print(type(d))
    if b=="s":
        e=int(input("Enter number for set :"))
        f=set()
        for g in range(e):
            h=int((input("Enter number :")))
            f.add(h)
        print(f)
        print(type(f))
    if b=="d":
        j=int(input("Enter the number for dict :"))
        z={}
        for m in range(j):
            k=int(input("Enter key :"))
            v=int(input("Enter value :"))
            z.update({k:v})
        print(z)
        print(type(z))
    if b=="t":
        l=[]
        p=int(input("Enter the number for tuple :"))
        for q in range(p):
            l.append(int(input("Enter number :")))
        l=tuple(l)
        print(l)
        print(type(l))
