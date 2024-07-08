# Task-2:Calculator

print("...Calculator...\n")

try:
    while True: 
       print("1.  Addition \n2.  Subtration  \n3.  Multiplication \n4.  Division \n5.  Exit\n")  
       ch=int(input("Enter your choice : "))
       
     
       if ch==1:
            a=int(input("Enter first number : "))
            b=int(input("Enter second number : "))
            print(a+b)
            print("\n")
            #    break
       elif ch==2:
            a=int(input("Enter first number : "))
            b=int(input("Enter second number : "))
            print(a-b)
            print("\n")
            #    break
       elif ch==3:
            a=int(input("Enter first number : "))
            b=int(input("Enter second number : "))
            print(a*b)
            print("\n")
            #    break
       elif ch==4: 
            a=int(input("Enter first number : "))
            b=int(input("Enter second number : "))
            print(a/b)
            print("\n")
            #    break
       else :
            break  
except:
    print("Enter valid value")                
