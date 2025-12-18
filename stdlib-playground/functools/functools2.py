from functools import reduce, singledispatch, singledispatchmethod
import operator

def factorial(n):
	return reduce(operator.mul, range(1, n + 1))
print(factorial(5))
# like itertools.accumulate, but returns only the last value


"generic function = A function composed of multiple functions implementing the same operation for different types." 
"                   Which implementation should be used during a call is determined by the dispatch algorithm."
"single dispatch = Generic func dispatch where the implementation is chosen based on the ~type~ of a single argument."
from typing import Union

class Negator:
	@singledispatchmethod
	@classmethod
	def neg(cls, arg):
		raise NotImplementedError(f'Cannot negate {arg}')

	@neg.register
	@classmethod
	def _(cls, arg: bool):
		return not arg

	@neg.register(Union[int, float, complex]) # alternative way
	@classmethod
	def sadi(cls, arg):
		return -arg

	@classmethod
	def nothing(cls, arg): # pre-existing func
		return 'Nothing.'
	neg.register(type(None), nothing)

n = Negator()
print(n.neg(5))
# for classes need to inspect the dispatcher itself before it's bound
print(Negator.__dict__['neg'].dispatcher.registry.keys()) # func.registry.keys() for singledispatch
print(Negator.__dict__['neg'].dispatcher.dispatch(int)) # func.dispatch(<type>) for singledispatch


