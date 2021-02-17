'''
    Author: Shaik Faizan Roshan Ali
    Date : 17th Feb 2021
    Email : alsahercoder@gmail.com
    Description : Print the infix of a mathematical equation in post fix form.
    
    Approach:
            - As we iterate through the array, we print operands.
            - Whenever we find an operator, we check if the precedence
              values is greater, equal or less than the current operator.
            - if current operator value preceds the existing top value of stack
            - add the current operator to the stack.
            - else, pop the existing pop operator until we find an operator precedence
            - value less than current operator value or stack is empty.
            
            - Parentheses case,
            - Open parentheses are given precedence value 0
            - Add '(' them to the operator stack, when found
            - When ')' close parentheses are found.
            - Dump all the operators until we find '(' or stack is empty
    
'''


def dumpOperators(operatorStack):
    
    ''' 
        Dumps all the operator until the last open
        parentheses or emptying of the list.
    '''
    while len(operatorStack) != 0:
        
        if operatorStack[-1] != '(':
        
            byebye = operatorStack[-1] 
            operatorStack.pop()
            print(byebye, end = " ")
        else:
            operatorStack.pop()
            break
        
def checkPrecedence(stack, operatorStack, current):
    
    precedence = {'+' : 1, '-' : 1, '*' : 2, '/' : 2, '(' : 0}
    
    if current.isdigit():
        return
    elif current == ')':
        
        ''' 
            When we find close parentheses we dump all the
            operators until the last open parentheses.
        '''
        dumpOperators(operatorStack)
        
    elif current == '(':
        operatorStack.append('(')
        
    elif len(operatorStack) != 0:
        if precedence[current] > precedence[operatorStack[-1]]:
            # push
            operatorStack.append(current)
        elif precedence[current] <= precedence[operatorStack[-1]]:
        
            '''
                 After removing the higher precedence, we check if there are
                 values that match the current precedence value.
                 if matched, we remove the rest of them.
            '''
            while precedence[current] <= precedence[operatorStack[-1]]:
                
                print(operatorStack[-1], end = " ")
                operatorStack.pop()
                ''' check if there are no elements so, we can add the current after pops'''
                if len(operatorStack) == 0:
                    break
                    
            operatorStack.append(current)
    
    else:
        operatorStack.append(current)

    
def doAllTheThings(equ): 
    
    operatorStack = []
    for y in equ:
        
        if y.isdigit():
            print(y, end =" ")
        else:
            checkPrecedence(equ, operatorStack, y)
    
    dumpOperators(operatorStack)
        
if __name__ == "__main__":

    tt = int(input())
    
    for i in range(0, tt):
        arr = input().split()
        size = len(arr)
        
        doAllTheThings(arr[:size-1])
        print()
