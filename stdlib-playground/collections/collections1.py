# https://code.activestate.com/recipes/305268/
# import UserDict

# class Chainmap(UserDict.DictMixin):
#     """Combine multiple mappings for sequential lookup.

#     For example, to emulate Python's normal lookup sequence:

#         import __builtin__
#         pylookup = Chainmap(locals(), globals(), vars(__builtin__))        
#     """

#     def __init__(self, *maps):
#         self._maps = maps

#     def __getitem__(self, key):
#         for mapping in self._maps:
#             try:
#                 return mapping[key]
#             except KeyError:
#                 pass
#         raise KeyError(key)

from collections import ChainMap

d1 = {'a':1, 'b':2}
d2 = {'a':3, 'd':4}

if __name__ == "__main__":
    cm = ChainMap(d1, d2)
    assert cm['a'] == 1
    assert cm['b'] == 2
    assert cm.get('a', 10) == 1 # key, default
    assert cm.get('b', 20) == 2
    assert cm.get('d', 30) == 4
    assert cm.get('f', 40) == 40

    d2.update(d1) # copies the dicts (O(n), doesn't know of original dict changes)
    print(d2)

#my tests
d1 = {"config": {"color": "white"}}
d2 = {"config": {"color": "red", "stop": False}}

cm = ChainMap(d1, d2)
print(cm["config"])   # {'theme': 'light'} , overwrites config at lvl 1

# GPT-5 examples:
# Configuration layering
defaults = {"theme": "light", "autosave": True}
user = {"theme": "dark"}
env = {"autosave": False}

settings = ChainMap(env, user, defaults)

print(settings["theme"])     # "dark" (from user)
print(settings["autosave"])  # False (from env)


# Dynamic context switching
cm = ChainMap({"x": 1})
print(cm["x"])  # 1
# Add a new scope
cm = cm.new_child({"x": 42})
print(cm["x"])  # 42
# Pop back
cm = cm.parents
print(cm["x"])  # 1
