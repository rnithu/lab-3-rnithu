#!/usr/bin/env python3

'''Lab 3 - free disk space function'''

# Any line that starts with a "#" is also known as a comment,
# these lines are ignored by the python interpreter even if
# they contain code. The very first line is called a Shebang line, 
# it is used to tell the system which interpreter to 
# use(python2, python3, bash, etc). 

# Author: Nithurshan Raveendran
# Author ID: 188141212
# Date Created: 2024/09/25

import subprocess

def free_space():
    # Run the command to get free disk space
    command = "df -h | grep '/$' | awk '{print $4}'"
    p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    
    # Capture the output
    output = p.communicate()
    
    # Convert stdout from bytes to a string, strip newlines
    free_space = output[0].decode('utf-8').strip()
    
    return free_space

if __name__ == '__main__':
    # Print the free space
    print(free_space())