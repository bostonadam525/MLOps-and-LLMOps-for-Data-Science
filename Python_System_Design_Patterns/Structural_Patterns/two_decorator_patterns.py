## uses 2 decorators applied to 1 function

from functools import wraps

def make_blink(function):
	"""Defines the decorator"""

	#This makes the decorator transparent in terms of its name and docstring
	@wraps(function)

	#Define the inner function
	def decorator():
		#Grab the return value of the function being decorated
		ret = function()

		#Add new functionality to the function being decorated
		return "<blink>" + ret + "</blink>"

	return decorator

#Your decorator code to make the text bold goes here
def make_bold(function):
	"""Defines the decorator"""

	#This makes the decorator transparent in terms of its name and docstring
	@wraps(function)

	#Define the inner function
	def decorator():
		#Grab the return value of the function being decorated
		ret = function()

		#Add new functionality to the function being decorated
		return "<b>" + ret + "</b>"

	return decorator

#Your code to apply the decorators goes here!
@make_blink
@make_bold
def hello_world():
	"""Original function! """

	return "Hello, World!"

def apply_decorators():
    return hello_world()
