from typing import Optional, List, DefaultDict
from collections import Counter, OrderedDict, deque
from sortedcontainers import SortedDict, SortedList
from itertools import permutations
from copy import copy
import heapq, math, statistics

def func_call_with_two_lists(a, b, obj):
    for func, args in zip(a[1:], b[1:]):
        print(getattr(obj, func)(*args))