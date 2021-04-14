'''
    Author: Shaik Faizan Roshan Ali
    Date: 20th Feb 2021
    Description: Evaluates the postfix form of the expression

    Approach:
            - As we iterate through the eqution from L -> R
            - we push operands into the stack
            - when operator is found
            - pop the top two elements in the stack
            - perform the operation with its respective operator
            - push the result into the stack and continue till the end
'''
Digitstack = []

def dealWithOperators(operator):

    global Digitstack
    result = 0
    if len(Digitstack) != 0:

        secondNum = int(Digitstack.pop())
        firstNum = int(Digitstack.pop())
        
        if operator == '+':
            result = firstNum + secondNum
        elif operator == '-':
            result = firstNum - secondNum
        elif operator == '*':
            result = firstNum * secondNum
        elif operator == '/':
            result = firstNum / secondNum

        Digitstack.append(result)
    else:
        print("SYNTAX ERROR")
    
    return result

def dealWithDigits(num):

    global Digitstack
    Digitstack.append(num)

def doAllTheThings(equ):

    output = 0
    for index in range(0, len(equ)):

        if equ[index].isdigit():
            dealWithDigits(equ[index])
        else:
            output = dealWithOperators(equ[index])
    print(output)         

if __name__ == "__main__":

      equ = input().split()
      doAllTheThings(equ)
