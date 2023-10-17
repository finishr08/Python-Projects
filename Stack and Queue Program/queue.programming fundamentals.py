##Queue in the list
##Mustafa Ahmed
##BSSE-08
##Programming Fundamentals

l=[]
while True:
    print("==========Queue Program==========")
    c=int(input("""
1 Push Element
2 Pop First Element
3 First Element
4 last Element
5 Display Element
6 Exit
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
            del l[0]
            print("New list: ",l)
    if c==3:
        if len(l)==0:
            print("==================")
            print("Empty Stack")
        else:
            print("==================")
            print("First Queue Value: ",l[0])
    if c==4:
        print("==================")
        print("Last Queue Value: ",l[-1])
    if c==5:
        print("==================")
        print("Display Queue: ",l)
    if c==6:
        print("==================")
        print("Now Queue Program is Exit")
        break

            
        
