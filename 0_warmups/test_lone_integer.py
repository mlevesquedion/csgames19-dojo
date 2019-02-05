from itertools import permutations
from lone_integer import lone_integer


def test_one_element():
    el = 1
    V = [el]
    assert lone_integer(V) == el


def test_order_independence():
    el = -1
    other = 2
    V = [el, other, other]
    for p in permutations(V):
        assert lone_integer(V) == el


def test_large_vector():
    el = 1234
    pos = 100
    V = list(range(100)) * 2
    tmp = V[pos]
    V[pos] = el
    V.append(tmp)
    assert lone_integer(V) == el
