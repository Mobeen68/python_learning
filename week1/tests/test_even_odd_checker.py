from ..even_odd_checker import isEven

def test_even():
    assert isEven(2) == True
    
def test_odd():
    assert isEven(3) == False
    
def test_zero():
    assert isEven(0) == 0