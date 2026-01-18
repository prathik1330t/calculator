from calculator import sum


def test_all_operations():
    add, sub, mul, div = sum(10, 5)

    assert add == 15
    assert sub == 5
    assert mul == 50
    assert div == 2
