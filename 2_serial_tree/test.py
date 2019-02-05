from bintree import Node
from serial_tree import serialize, deserialize
from pytest import mark

if __name__ == "__main__":
    def identity(tree):
        return deserialize(serialize(tree))

    tree1 = Node(1, None, None)
    tree2 = Node(1, Node(2, Node(3, Node(4, None, None), None), None), None)
    tree3 = Node(5, Node(2, None, None), Node(
        9, Node(6, None, None), Node(11, None, None)))

    assert tree1 == identity(tree1)
    assert tree2 == identity(tree2)
    assert tree3 == identity(tree3)
