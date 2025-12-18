from functools import update_wrapper, wraps

# A dead simple decorator

def my_first_decorator(f):
	def wrapper():
		print('Before function runs')
		f()
		print('After function runs')
	return wrapper

@my_first_decorator
def hello_wrold():
	print('Hello, world!')

hello_wrold()


# update_wrapper and wraps make the wrapper look like the original function (wrapped)

def deco(func):

	@wraps(func)
	def wrapper(*args, **kwargs):
		# do something useful
		func(*args, **kwargs)
	return wrapper

@deco
def yo(who):
	"""Docstring 8
	a decorated function
	"""
	print('Yo', who)

yo('Everyone')
print('Name:', yo.__name__, '-', yo.__doc__) # @wraps keeps those


# no sugar
def raw_deco(f):
	def wrapper():
		print('I was here')
		#f()        # call and return wrapper, which returns None implicitly
		#return f   # return function object
		return f() # return result from called function 
	return wrapper
print('----------------------')
raw_deco('')
# Python behind the scenes:
# hello_wrold = raw_deco(hello_wrold) 
print(raw_deco(hello_wrold)()) # raw_deco(hello_wrold) -> returns wrapper, so needs to be called
