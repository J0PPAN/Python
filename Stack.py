"""Menu Driven Stack to perform all necessary Operations"""
def menu():             #Function Definition Statement
    print("\nMENU")
    print("~~")
    print("1.Push\n2.Pop\n3.Display\n4.Exit")
    
stack=[]                    #Intializing List for Stacking
print("\n\t\tMenu Driven Stack")
print("\t\t~~~~~~~")
i = 0
while True:
    menu()                  #Function Calling 
    ch=int(input("\nEnter your choice:"))
    if ch==1:
        Name=input("Enter the City Name:")          #Accepting Data from User
        Pin=input("Enter the Pin code:")
        Directory = (Name,Pin)
        stack.insert(i,Directory)        #Appending Directory to Stack
        print("Pushed successfully!")
        i=i+1
        
    elif ch==2:
        if stack==[]:                   #Checking Underflow Condition
            print("Underflow Occured; Cannot Pop from Empty Stack!!!")
        else:            
            print("Element",stack[-1],"has been popped.")
            stack.pop()             #Popping Last Appended Directory
            
    elif ch==3:
        if stack==[]:                   #Checking whether Stack is Empty
            print("The stack does not contain anything.")
        else:
            print(stack)
                
    elif ch==4:
        print("Exiting...")
        break                   #Exiting from Loop
    
    else:
        print("Invalid choice!")
