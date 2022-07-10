"""
Destructors in Python:
Destructors are called when an object gets destroyed.
In Python, destructors are not needed as much as in C++ because
Python has a garbage collector that handles memory management
automatically.
The __del__() method is a known as a destructor method in Python

"""

# Python program to illustrate destructor
class Employee:

    # Initializing
    def __init__(self):
        print("Employee created.")

    # Deleting (Calling destructor)
    def __del__(self):
        print("Destructor called, Employee deleted.")


# obj = Employee()
# del obj

#  OutPut: Employee created.
#   Employee created.
#   Destructor called, Employee deleted.

# 2.

class Employee:

    # Initializing
    def __init__(self):
        print('Employee created')

    # Calling destructor
    def __del__(self):
        print("Destructor called")

def Create_obj():
    print('Making Object...')
    obj = Employee()
    print('function end...')
    return obj

print('Calling Create_obj() function...')
obj = Create_obj()
print('Program End...')

#OutPut:
    # Calling Create_obj() function...
    # Making Object...
    # Employee created
    # function end...
    # Program End...
    # Destructor called
























