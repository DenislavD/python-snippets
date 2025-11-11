from collections import deque, namedtuple
import itertools
import sys

my_deq = deque([1, 2, 3, 4, 5], 5)
print('1:', my_deq)

my_deq.appendleft(6)

print('2:', my_deq)

res = my_deq.count(2)
res = my_deq.index(3, 0, 15) # index(x[, start[, stop]])
print('Res:', res)

def tail(filename, n=10):
    'Return the last n lines of a file'
    with open(filename) as f:
        return deque(f, n)

# moving average - sliding window algo
seq = [10, 20, 30, 40, 50, 60, 70, 80, 10]
def mov_avg(namba: int):
    it = iter(seq) # add a stateful element pointer
    d = deque(itertools.islice(it, namba-1))
    d.appendleft(0) # workaround for first item
    # it pointer is at index 3 now (40)
    sum_ = sum(d)
    print(d)
    for item in it:
        sum_ += item - d.popleft() # walking sum
        d.append(item)
        print('Curr. sum:', sum_)
        yield sum_ / namba

print(list(mov_avg(4)))


# namedtuple, dataclass
my_tuple = ('Kori', 'Sadi', 'Alendi')
print(my_tuple)
Point = namedtuple('Pointz', ['x', 'y']) # declaring namedtuple
p = Point(11, y=22)
print(p)
Point3D = namedtuple('Point3D', Point._fields + ('z',)) # for new fields make another one, don't extend class
print(Point3D(1, 2, 3))

import csv
import os

parent_dir = os.path.dirname(os.path.dirname(__file__))
my_path = os.path.join(parent_dir, 'basics', 'locations.csv')

Mini_Wizard = namedtuple('Mini_Wizard', 'name, home')

with open(my_path, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        # print(row)
        # continue
        mw = Mini_Wizard(*row) # or Mini_Wizard._make(row) # - accepts a list
        print(mw)

Account = namedtuple('Account', ['type', 'balance', 'rank'], defaults=[0, 2])
print(Account._field_defaults)
print(Account('premium',))

# dataclass example
from dataclasses import dataclass # 3.7+

@dataclass
class Mini_Wizard_DC:
    name: str
    home: str

wizard = Mini_Wizard_DC('Sali', 'L.A.')
print(wizard)
wizard.name = 'Ron' # mutable
print(wizard.name)