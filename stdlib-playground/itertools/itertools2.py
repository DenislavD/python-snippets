from itertools import repeat, islice, pairwise, starmap, tee, zip_longest, takewhile

# Iterator slice - lazy processing, doesn't load everything in memory

large_list = iter(range(1000000)) # iter to keep the pointer !!! <3
for i in range(5):
	print(list(islice(large_list, 5)))

# pairwise
prices = [100, 105, 103, 110, 108]
for prev, curr in pairwise(prices):
	change = curr - prev
	print(f"{prev} → {curr}: {'📈' if change > 0 else '📉'} {change:+d}")

# map and starmap

# 1 to 10 with **2 each, supplies arguments in parallel
print(list(map(pow, range(10), repeat(2))))

# already prearranged in tuples - use starmap, supplies them in tuples
my_list = [(0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2),]
print(list(starmap(pow, my_list)))


# tee - iterator duplication
def lookahead(tee_iterator):
	"Return the next value without moving the input forward"
	[forked_iterator] = tee(tee_iterator, 1)
	return next(forked_iterator)

iterator = iter('abcdef')
iterator, *_ = tee(iterator, 5) # UNPACKING - take the first element from the tuple and assign it to iterator
print(iterator)

# zip_longest
names = ['Alexy', 'Pecko', 'Jodi', 'Kori', 'Raly', ]
positions = iter(range(1, 50))

res = takewhile(lambda x: x[1] < 7, zip_longest(names, positions, fillvalue='-'))
print(list(res))