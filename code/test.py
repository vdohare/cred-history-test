import test

def test_add_1():
    assert test.add(2, 3) == 5
    assert test.add(-1, 1) == 0
    assert test.add(0, 0) == 0

def test_subtract():
    assert test.subtract(5, 2) == 3
    assert test.subtract(1, -1) == 2
    assert test.subtract(0, 0) == 0

def test_multiply():
    assert test.multiply(2, 3) == 6
    assert test.multiply(-1, 1) == -1
    assert test.multiply(0, 5) == 0

def test_divide():
    assert test.divide(6, 3) == 2
    assert test.divide(5, 2) == 2.5
    try:
        test.divide(1, 0)
        assert False, "Expected ZeroDivisionError"
    except ZeroDivisionError:
        pass

if __name__ == "__main__":
    test_add()
    test_subtract()
    test_multiply()
    test_divide()
    print("All tests passed!")
