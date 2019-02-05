from hardcore_anagram_difference import hardcore_anagram_difference
from pytest import mark


@mark.parametrize(
    ['words', 'expected'],
    [
        ({''}, 0),
        ({'abc'}, 0),
        ({'', ''}, 0),
        ({'a', ''}, 1),
        ({'', 'a'}, 1),
        ({'ab', 'a'}, 1),
        ({'ab', 'ba'}, 0),
        ({'ab', 'cd'}, 4),
        ({'codewars', 'hackerrank'}, 10),
        ({'a', '', ''}, 1),
        ({'a', 'b', 'c'}, 3),
        ({'abc', 'ab', 'a'}, 3),
        ({'hello', 'hola', 'allo'}, 7),
        ({'cat', 'dog', 'mouse'}, 11),
        ({'mouse', 'house', 'hose', 'host'}, 10)
    ]
)
def test_anagram_difference(words, expected):
    assert hardcore_anagram_difference(words) == expected
