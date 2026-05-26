import test

def test_add():
    assert test.add(2, 3) == 5
    assert test.add(-1, 1) == 0
    assert test.add(0, 0) == 0

def test_subtract():
    assert test.subtract(5, 2) == 3
    assert test.subtract(1, -1) == 2
    assert test.subtract(0, 0) == 0

if __name__ == "__main__":
    test_add()
    test_subtract()
    test_multiply()
    test_divide()
    print("All tests passed!")
