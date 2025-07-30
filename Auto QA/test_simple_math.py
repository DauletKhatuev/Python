import pytest
class SimpleMath:
    """Класс с простыми математическими операциями."""

    def square(self, x):
        """Возвращает квадрат числа."""

        return x * x

    def cube(self, x):
        """Возвращает куб числа."""

        return x * x * x


def test_square():
    square = SimpleMath()
    res = square.square(2)

    assert res == 4

def test_cube():
    cube = SimpleMath()
    res = cube.cube(-3)

    assert res == -27

