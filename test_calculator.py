from calculator import sum

def test_add():
    assert sum(10,5)==15

def test_sub():
    assert sum(10,5)==5

def test_mul():
    assert sum(10,5)==50

def test_div():
    assert sum(10,5)==2
