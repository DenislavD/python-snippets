from itertools import chain, starmap, repeat, islice
from collections import deque
# cool recipes

def prepend(value, iterable):
	# prepend(1, [2, 3, 4,]) -> 1 2 3 4
	return chain([value], iterable)
print(list(prepend(1, iter('abvc')))) # works with iterators as well

def tabulate(func, start=0):
	# Return func(0), func(1), ...
	return map(func, count(start))

def repeat_func(func, times=None, *args):
	# Repeat calls to a function with specified arguments
	if times is None:
		return starmap(func, repeat(args))
	return starmap(func, repeat(args, times))

flatten = chain.from_iterable([[1, 2,], [3, 4,], [5, [6]]])
print(list(flatten)) # flatten one level

for _ in repeat(None, 4):
	print('A?', end=' ')

def tail(n, iterable):
	# tail(3, 'ABCDEFG') -> E F G (efficient memory use - n items in a fixed-size buffer, streaming-friendly)
	return iter(deque(iterable, maxlen=n))
print(list(tail(3, range(100000)))) # iter above and list here can be skipped in this example

def consume(iterator, n=None):
	# consume iterators at C speed
	if n is None:
		deque(iterator, maxlen=0)
	else:
		# cuts the first n elements, then triggers the "cut" with next()
		# the next on an empty iterator returns None here, next item remains n
		next(islice(iterator, n, n), None) # start, stop at n

def nth(iterable, default=None):
	return next(islice(iterable, n, None), default) # islice STOPS at n, next returns it

def quantify(iterable, predicate=bool):
	"Given a predicate that returns True or False, count the True results."
	return sum(map(predicate, iterable))
