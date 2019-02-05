
from pytest import mark
from stars import solve


@mark.parametrize(
    ['parens', 'expected'],
    (
        ['*', True],
        ['(*', True],
        ['*)', True],
        ['(*)', True],
        [')*(', False],
        ['(()*', True],
        ['(*)*(*', True],
        ['(((*)', False],
        ['(((*))', True],
        ['(***()*)()*()(*))', True],
        ['(************))))', True],
    )
)
def test_stars(parens, expected):
    assert solve(parens) == expected
