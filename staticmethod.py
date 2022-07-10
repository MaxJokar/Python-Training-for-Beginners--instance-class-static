"""
Static Methods in Python
"""
class DecoratorExample:

  def __init__(self):
    print('Hello, World!')


  """ This method is a static method!
    The @staticmethod decorator  tells Python that
    this method is a static method.
  """
  @staticmethod  #  Here without this decorator also works!
  def example_function():
    print('I\'m a static method!')

de = DecoratorExample.example_function()

#  OutPut:  I'm a static method!