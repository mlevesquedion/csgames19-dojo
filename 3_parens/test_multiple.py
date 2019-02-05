from pytest import mark
from multiple import solve


@mark.parametrize(
    ['parens', 'expected'],
    (
        ['({}[]){{[[]]((()))}}', True],
        ['({}[]){{[[]](()))}}', False],
    )
)
def test_multiple(parens, expected):
    assert solve(parens) == expected
