from anagram_difference import anagram_difference
from pytest import mark


@mark.parametrize(
    ['left', 'right', 'expected'],
    [
        ('', '', 0),
        ('a', '', 1),
        ('', 'a', 1),
        ('ab', 'a', 1),
        ('ab', 'ba', 0),
        ('ab', 'cd', 4),
        ('codewars', 'hackerrank', 10),
        ('abcgklmmnooooprsuvwx',
         'efijklmprrrrsuvvxxxxz', 23)
    ]
)
def test_anagram_difference(left, right, expected):
    assert anagram_difference(left, right) == expected
