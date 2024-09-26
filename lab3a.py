#!/usr/bin/env python3

# Any line that starts with a "#" is also known as a comment,
# these lines are ignored by the python interpreter even if
# they contain code. The very first line is called a Shebang line, 
# it is used to tell the system which interpreter to 
# use(python2, python3, bash, etc). 

# Author: Nithurshan Raveendran
# Author ID: 188141212
# Date Created: 2024/09/25

def return_text_value():
    name = 'Terry'
    greeting = 'Good Morning ' + name
    return greeting

def return_number_value():
    num1 = 10
    num2 = 5
    num3 = num1 + num2
    return num3

if __name__ == '__main__':
    print('python code')
    text = return_text_value()
    print(text)
    number = return_number_value()
    print(str(number))