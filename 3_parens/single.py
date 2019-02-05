def solve(x):
    lefts = 0
    for c in x:
        if c == '(':
            lefts += 1
        if c == ')':
            if lefts:
                lefts -= 1
            else:
                return False
    return lefts == 0
