def square(x):
    return x * x


def test_square():
    assert square(2) == 4
    assert square(-3) == 9
    assert square(0) == 0

def test_square_zero():
    assert square(2) == 4
