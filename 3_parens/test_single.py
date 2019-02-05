from pytest import mark
from single import solve


@mark.parametrize(
    ['parens', 'expected'],
    (
        ['(', False],
        [')', False],
        ['()', True],
        ['()()', True],
        ['(())', True],
        ['())(', False],
        ['())))', False],
        ['(((()', False],
        ['(())()((()))', True],
        ['(())()())()))()()', False]
    )
)
def test_single(parens, expected):
    assert solve(parens) == expected
