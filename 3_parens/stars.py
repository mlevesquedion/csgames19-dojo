from quicktest import test


def solve(x):
    lefts, stars = 0, 0
    for c in x:
        if c == '(':
            lefts += 1
        if c == '*':
            stars += 1
        if c == ')':
            if lefts:
                lefts -= 1
                continue
            if stars:
                stars -= 1
                continue
            return False
    return lefts <= stars


if __name__ == '__main__':
    test(solve,
         [
             ['(()*', True],
             ['(***()*)()*()(*))', True],
             ['(************))))', True],
             ['(*)', True],
             ['(*)*(*', True],
             ['(((*)', False],
             ['(((*))', True],
             [')*(', False]
         ])
