from collections import Counter, defaultdict

cnt = Counter() # arg= iterable or mapping

for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
    cnt[word] += 1 # mapping

print(cnt)
print(cnt['BLACK']) # 0


import re
import os

parent_dir = os.path.dirname(os.path.dirname(__file__))
words = re.findall(r'\w+', open(os.path.join(parent_dir, 'HI.txt')).read().lower())

most_common = Counter(words).most_common(10)[:-6:-1] # in-place class instantiation with iterable list
print(most_common) # in tuples

# support rich comparison operators
# so Counter(a=1) == Counter(a=1, b=0) returns True

c = Counter(a=3, b=1)
d = Counter(a=1, b=2)
c + d                       # add two counters together:  c[x] + d[x]
c - d                       # subtract (keeping only positive counts)
c & d                       # intersection:  min(c[x], d[x])
c | d                       # union:  max(c[x], d[x])
c == d                      # equality:  c[x] == d[x]
c <= d                      # inclusion:  c[x] <= d[x]

c = Counter(a=2, b=-4)
+c # Counter({'a': 2})
-c # Counter({'b': 4})


def_dict = defaultdict(list)
for k, v in most_common:
    def_dict[k].append(v) # empty list created by list default_factory provided at instantiation
def_dict['a'].append(6)
print(def_dict['a'])

def constant_factory(value):
    return lambda: value # needs to return a callable
dd = defaultdict(constant_factory('<missing>'))
dd.update(name='John', action='ran')
print('%(name)s %(action)s to %(object)s' % dd)