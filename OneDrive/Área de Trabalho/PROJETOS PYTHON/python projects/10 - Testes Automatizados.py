import pytest

def soma(a, b):
    return a + b

def test_soma():
    assert soma(3, 4) == 7
    assert soma(-1, 1) == 0

if __name__ == '__main__':
    pytest.main()

    