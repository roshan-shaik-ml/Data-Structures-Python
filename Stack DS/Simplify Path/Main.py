from Stack import Stack


def solve(string):

    stack = Stack()
    filename = ""
    index = 0
    while index < len(string):

        if string[index] != '/' and string[index] != '.':

            filename += string[index]
        elif filename != "":

            stack.push(filename)
            filename = ""

        if index !=  len(string) - 1:
            
                if string[index] == "." and string[index+1] == ".":

                stack.pop()
        index += 1
    
    path = ""
    if stack.isEmpty():
        path = "/"
    
    for i in range(0, len(stack.stack)):

        path += "/" + stack.stack[i]
    return path
        
            

if __name__ == "__main__":

    string = "/home//foo/"
    solve(string)