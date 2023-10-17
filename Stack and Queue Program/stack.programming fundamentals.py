##stack in the list
##Mustafa Ahmed
##BSSE-08
##Programming Fundamentals

l=[]
while True:
    print("==========Stack Program==========")
    c=int(input("""
1 Push Element
2 Pop Element
3 Last Element
4 Display Element
5 Exit
"""))
    if c==1:
        n=input("Enter the Push Element: ")
        l.append(n)
        print("==================")
        print(l)
    if c==2:
        if len(l)==0:
            print("Empty Stack")
        else:
            print("==================")
            print("Given list: ",l)
            p=l.pop()
            print(p)
            print("New list: ",l)
    if c==3:
        if len(l)==0:
            print("==================")
            print("Empty Stack")
        else:
            print("==================")
            print("Last Stack Value: ",l[-1])
    if c==4:
        print("==================")
        print("Display Stack: ",l)
    if c==5:
        print("==================")
        print("Now Stack Program is Exit")
        break
            
        
