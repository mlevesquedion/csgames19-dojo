def solve(x):
    stack = []
    pairs = {left: right for left, right in '() {} []'.split()}
    for c in x:
        if c in pairs:
            stack.append(c)
        else:
            if stack and pairs[stack[-1]] == c:
                stack.pop()
            else:
                return False
    return not stack
