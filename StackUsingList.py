#    
#    Author : Shaik Faizan Roshan Ali
#    Date : 2nd Feb 2021
#    Email : alsahercoder@gmail.com
#    Program for stacks using lists. 
#    Note: Lists can be slow when handling large amounts of data.
#

def stackPush(data):
    stack.append(data)
    print(stack)
    
def stackPop():
    stack.pop()
    print(stack)

stack = []

option = -1
while(option != 0):

    print("******Select a number for operation******")
    print("\t0. Exit")
    print("\t1. Push")
    print("\t2. Pop")

    option = int(input("Enter your option: "))
    
    if option == 1:
        stackPush(input("Insert your value: "))
        
    elif option == 2:
        stackPop()
        
    elif option == 0:
        break
    else:
        print("NOT VALID")
