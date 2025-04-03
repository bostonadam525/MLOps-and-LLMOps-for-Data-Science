## decorator pattern in python
from functools import wraps

def make_blink(function):
    """Defines a decorator"""

    # This makes the decorator transparent in terms of its name and docstring.
    @wraps(function)


    # Define inner function definition
    def decorator():
        # Grab return value of function being decorated
        ret = function()


        # Add new functionality to function being decorated
        return "<blink>" + ret + "</blink>"


    return decorator

# Apply new decorator here!
@make_blink
def hello_world():
    """Original function!"""

    return "Hello, World!"

# check result of decorating
print(hello_world())

# check if function name is still same name of function being decorated
print(hello_world.__name__)

# check if docstring is still same as that of function being decorated
print(hello_world.__doc__)



