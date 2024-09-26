#!/usr/bin/env python3

'''Lab 3 Inv 2 function operate '''

# Any line that starts with a "#" is also known as a comment,
# these lines are ignored by the python interpreter even if
# they contain code. The very first line is called a Shebang line, 
# it is used to tell the system which interpreter to 
# use(python2, python3, bash, etc). 

# Author: Nithurshan Raveendran
# Author ID: 188141212
# Date Created: 2024/09/25

def operate(number1, number2, operator):
    
    if operator == 'add':
        result = number1 + number2
    elif operator == 'subtract':
        result = number1 - number2
    elif operator == 'multiply':
        result = number1 * number2
    else:
        result = 'Error: function operator can be "add", "subtract", or "multiply"'
    
    return result

if __name__ == '__main__':

    print(operate(10, 5, 'add'))        
    print(operate(10, 5, 'subtract'))   
    print(operate(10, 5, 'multiply'))   
    print(operate(10, 5, 'divide'))     