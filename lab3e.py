#!/usr/bin/env python3

# Create the list called "my_list" here, not within any function defined below.
# That makes it a global object. We'll talk about that in another lab.

# Any line that starts with a "#" is also known as a comment,
# these lines are ignored by the python interpreter even if
# they contain code. The very first line is called a Shebang line, 
# it is used to tell the system which interpreter to 
# use(python2, python3, bash, etc). 

# Author: Nithurshan Raveendran
# Author ID: 188141212
# Date Created: 2024/09/25

my_list = [100, 200, 300, 'six hundred']

def give_list():
    """Returns all of the items in the global object my_list unchanged."""
    return my_list

def give_first_item():
    """Returns the first item in the global object my_list as a string."""
    return str(my_list[0])

def give_first_and_last_item():
    """Returns a list that includes the first and last items in the global object my_list."""
    return [my_list[0], my_list[-1]]

def give_second_and_third_item():
    """Returns a list that includes the second and third items in the global object my_list."""
    return my_list[1:3]

if __name__ == '__main__':
    print(give_list())  
    print(give_first_item())  
    print(give_first_and_last_item())  
    print(give_second_and_third_item())  