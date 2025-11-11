# LRU time-bound algo with OrderedDict
from collections import OrderedDict, UserDict, UserList, UserString # wrappers, can add my methods, .data
from time import time

class OrderedDictLRUCache:
    "LRU Cache that invalidates and refreshes old entries."

    def __init__(self, func, maxlength=2, maxage=30):
        self.func = func
        self.cache = OrderedDict() # instance? {args : (timestamp, result)}
        self.maxlength = maxlength
        self.maxage = maxage

    def __call__(self, *args): # * here: pack args into a tuple of all arguments provided (not checked vs func definition)
        # Args: ('sad', 'A?')
        if args in self.cache: # can be like self.cache[('sad', 'A?', 'fail')] LOL
            self.cache.move_to_end(args) # refresh position as recently used in cache
            timestamp, result = self.cache[args] # unpack the dict tuple value
            if time() - timestamp <= self.maxage:
                return result
        # not found - call func
        result = self.func(*args) # * here: "unpack the tuple"
        self.cache[args] = time(), result # add to cache; comma = tuple : b = 1, 2, 3 (tuple)
        #print(self.cache[args]) : (1762876149.0509079, 'Result: ^^sad^^')   
        if len(self.cache) > self.maxlength:
            self.cache.popitem(last=False) # remove item FIFO (oldest)
        return result


# decorate with cache
@OrderedDictLRUCache
def add_hyphens(text, text2='text2'):
    print('called func')
    return 'Result: ^^' + text + '^^'

print(add_hyphens('sad', 'A?'))
print(add_hyphens('sad', 'A?')) # second call - will be delivered from cache (no called func)
print(add_hyphens('happy'))
print(add_hyphens('happier'))
print(add_hyphens('sad', 'A?')) # popped out as maxlength exceeded, runs func again

d = {'a': 3, 'b': 2, ('c', 'e'): 34}
if ('c', 'e') in d: 
    print('key found') # d[('c', 'e')] exists
else:
    print('key not found')

# @ClaudeAI: Multiple assignment (tuple unpacking)
x, y = 5, 10 # Right side creates tuple (5, 10), then unpacks
