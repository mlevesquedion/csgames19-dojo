class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other):
        return self.val == other.val and self.left == other.left and self.right == other.right

    def __str__(self):
        return f'Node({self.val},{self.left},{self.right})'

    def __repr__(self):
        return str(self)
