#!/usr/bin/env python3

# Any line that starts with a "#" is also known as a comment,
# these lines are ignored by the python interpreter even if
# they contain code. The very first line is called a Shebang line, 
# it is used to tell the system which interpreter to 
# use(python2, python3, bash, etc). 

# Author: Nithurshan Raveendran
# Author ID: 188141212
# Date Created: 2024/09/25

# Place my_list below this comment (before the function definitions)

my_list = [1, 2, 3, 4, 5]

def add_item_to_list(ordered_list):
    """Appends a new item to the end of the list with value (last item + 1)."""
    
    last_item = ordered_list[-1]
    ordered_list.append(last_item + 1)

def remove_items_from_list(ordered_list, items_to_remove):
    """Removes all items in items_to_remove list from ordered_list if they exist."""
    for item in items_to_remove:
        if item in ordered_list:
            ordered_list.remove(item)

# Main code
if __name__ == '__main__':
    print(my_list)  # Initial list
    add_item_to_list(my_list)  # Add item 6
    add_item_to_list(my_list)  # Add item 7
    add_item_to_list(my_list)  # Add item 8
    print(my_list)  # After adding items: should print [1, 2, 3, 4, 5, 6, 7, 8]
    remove_items_from_list(my_list, [1, 5, 6])  # Remove 1, 5, and 6
    print(my_list)  # After removing items: should print [2, 3, 4, 7, 8]