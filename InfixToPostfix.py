# cook your dish here
def dumpOperators(operatorStack, expression):
    
    ''' 
        Dumps all the operator until the last open
        parentheses or emptying of the list.
    '''
    while len(operatorStack) != 0:
        
        if operatorStack[-1] != '(':
        
            byebye = operatorStack[-1] 
            operatorStack.pop()
            expression.append(byebye)
        else:
            operatorStack.pop()
            break
        
def checkPrecedence(stack, expression, operatorStack, current):
    
    precedence = {'+' : 1, '-' : 1, '*' : 2, '/' : 2, '(' : 0}
    
    if current.isdigit():
        return
    elif current == ')':
        
        ''' 
            When we find close parentheses we dump all the
            operators until the last open parentheses.
        '''
        dumpOperators(operatorStack, expression)
        
    elif current == '(':
        operatorStack.append('(')
        
    elif len(operatorStack) != 0:
        if precedence[current] > precedence[operatorStack[-1]]:
            # push
            operatorStack.append(current)
        elif precedence[current] <= precedence[operatorStack[-1]]:
        
            '''
                 After removing the higher precedence, we check if there are
                 values that are equal to current precedence value.
                 if matched, we remove the rest of them.
            '''
            while precedence[current] <= precedence[operatorStack[-1]]:
                
                expression.append(operatorStack[-1])
                operatorStack.pop()
                ''' 
                    check if there are no elements so, 
                    we can add the current after pops
                '''
                if len(operatorStack) == 0:
                    break
                    
            operatorStack.append(current)
    
    else:
        operatorStack.append(current)
    
def doAllTheThings(equ): 
    
    operatorStack = []
    expression = []
    for y in equ:
        
        if y.isdigit() or y.isalpha():
            expression.append(y)
        else:
            checkPrecedence(equ, expression, operatorStack, y)
        
        print("expression: ", expression,"   stack", operatorStack)
    
    dumpOperators(operatorStack, expression)
    print("expression: ", expression,"   stack", operatorStack)
        
if __name__ == "__main__":

    tt = int(input())
    
    for i in range(0, tt):
        arr = input().split()
        size = len(arr)
        
        doAllTheThings(arr[:size-1])
        print()
