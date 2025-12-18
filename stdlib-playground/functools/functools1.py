from functools import cached_property, lru_cache, partialmethod
import statistics

class Dataset:
	def __init__(self, sequence_of_numbers):
		self._data = tuple(sequence_of_numbers)

	# for expensive, but immutable computed properties of instances
	# needs __dict__ or __slots__ with __dict__
	@cached_property
	def  stdev(self):
		return statistics.stdev(self._data)

ds = Dataset([1, 5, 10, 15, 20])
#print(ds.stdev)


@lru_cache
def count_vowels(sentence):
	return sum(sentence.count(vowel) for vowel in 'AEIOUaeiou')

count_vowels('Who let the AI out?')
count_vowels('Who let the AI out?') # hit
count_vowels('Who let the AI out')
print(count_vowels.__wrapped__('Who let the AI out')) # bypasses the cache

# info functions added to wrapped func
print(count_vowels.cache_parameters())
print(count_vowels.cache_info()) # cache analysis


# partialmethod
class Cell:
	def __init__(self):
		self._selected = False

	@property
	def selected(self):
		return self._selected
	
	def set_state(self, state):
		self._selected = bool(state)
	
	select = partialmethod(set_state, True) # method descriptors now ffs.. (have __get__)
	deselect = partialmethod(set_state, False)

c = Cell()
print('Selected:', c.selected)
c.select()
print('Selected:', c.selected)
#
print(type(c.select), hasattr(c.deselect, '__get__'), sep=', ')
