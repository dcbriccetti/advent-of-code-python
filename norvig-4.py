from __future__  import annotations
from collections import Counter, defaultdict, namedtuple, deque
from itertools   import permutations, combinations, product, chain
from functools   import lru_cache, reduce
from typing      import Dict, Tuple, Set, List, Iterator, Optional, Union, Sequence
from contextlib  import contextmanager

import operator
import math
import ast
import sys
import re

def data(day: int, parser=str, sep='\n') -> list:
    "Split the day's input file into sections separated by `sep`, and apply `parser` to each."
    with open(f'data/advent2020/input{day}.txt') as f:
        sections = f.read().rstrip().split(sep)
        return list(map(parser, sections))

def do(day, *answers) -> List[int]:
    "E.g., do(3) returns [day3_1(in3), day3_2(in3)]. Verifies `answers` if given."
    g = globals()
    got = []
    for part in (1, 2):
        fname = f'day{day}_{part}'
        if fname in g:
            got.append(g[fname](g[f'in{day}']))
            if len(answers) >= part:
                assert got[-1] == answers[part - 1], (
                    f'{fname}(in{day}) got {got[-1]}; expected {answers[part - 1]}')
        else:
            got.append(None)
    return got

Number = Union[float, int]
Atom = Union[Number, str]
Char = str # Type used to indicate a single character

cat = ''.join
flatten = chain.from_iterable

def quantify(iterable, pred=bool) -> int:
    "Count the number of items in iterable for which pred is true."
    return sum(1 for item in iterable if pred(item))

def first(iterable, default=None) -> object:
    "Return first item in iterable, or default."
    return next(iter(iterable), default)

def prod(numbers) -> Number:
    "The product of an iterable of numbers."
    return reduce(operator.mul, numbers, 1)

def dot(A, B) -> Number:
    "The dot product of two vectors of numbers."
    return sum(a * b for a, b in zip(A, B))

def ints(text: str) -> Tuple[int]:
    "Return a tuple of all the integers in text."
    return mapt(int, re.findall('-?[0-9]+', text))

def lines(text: str) -> List[str]:
    "Split the text into a list of lines."
    return text.strip().splitlines()

def mapt(fn, *args):
    "Do map(fn, *args) and make the result a tuple."
    return tuple(map(fn, *args))

def atoms(text: str, ignore=r'', sep=None) -> Tuple[Union[int, str]]:
    "Parse text into atoms separated by sep, with regex ignored."
    text = re.sub(ignore, '', text)
    return mapt(atom, text.split(sep))

def atom(text: str, types=(int, str)):
    "Parse text into one of the given types."
    for typ in types:
        try:
            return typ(text)
        except ValueError:
            pass

@contextmanager
def binding(**kwds):
    "Bind global variables within a context; revert to old values on exit."
    old_values = {k: globals()[k] for k in kwds}
    try:
        globals().update(kwds)
        yield # Stuff within the context gets run here.
    finally:
        globals().update(old_values)

Passport = dict # e.g. {'iyr': '2013', ...}

def parse_passport(text: str) -> Passport:
    "Make a dict of the 'key:val' entries in text."
    return Passport(re.findall(r'([a-z]+):([^\s]+)', text))

assert parse_passport('''a:1 b:two\nsee:3''') == {'a': '1', 'b': 'two', 'see': '3'}

in4: List[Passport] = data(4, parse_passport, '\n\n') # Passports are separated by blank lines

required_fields = {'byr', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid'}

def day4_1(passports): return quantify(passports, required_fields.issubset)

do(4)
