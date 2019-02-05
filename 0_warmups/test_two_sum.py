from two_sum import two_sum


def test_present():
    V = [1, 2, 3, 4]
    K = 6
    assert two_sum(V, K)


def test_absent():
    V = [10, 15, 3, 7]
    K = 15
    assert not two_sum(V, K)


def test_large_vector():
    V = list(range(1000))
    K = 1234
    assert two_sum(V, K)
