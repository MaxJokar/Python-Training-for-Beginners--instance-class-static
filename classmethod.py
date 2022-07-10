"""
Class methods can't access specific instance data,
but they can call other static methods.
"""


class DecoratorExample:
    """Example Class"""

    def __init__(self):
        print("Hello, World!")

    @classmethod
    def example_function(cls):
        """This method is a class method can access to static method !"""
        print("I'm a class method!")
        cls.some_other_function(20, 30)

    @staticmethod
    def some_other_function(numb_1, numb_2):
        print("Hello!")
        print(numb_1 + numb_2)


de = DecoratorExample()
de.example_function()


#  OutPut:
# Hello, World!
# I'm a class method!
# Hello!
