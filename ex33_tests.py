# TDD - Test Driven Development
# napisz testy do funkcji ktora ma obliczac iloczyn dwoch liczb
# uwzgledni przypadki kiedy:
# obie sa dodatnie
# obie sa ujemne
# jedna dodatnia druga ujemna
# jedna jest zerem
#
# napisz funkcje wykonujaca mnozenie
# sprawdz czy testy przechodza korzystajac z pytest


def test_multiplication_both_positive():
    assert multiplication(2,3) == 6

def test_multiplication_both_negative():
    assert multiplication(-2,-3) == 6

def test_multiplication_positive_and_negative():
    assert multiplication(-2,3) == -6
    assert multiplication(-1,5) == -5

def test_multiplication_one_is_zero():
    assert multiplication(2,0) == 0

def multiplication(a,b):
    return a*b
