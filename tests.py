# pytest - podstawowy modul do testow w pythonie
# pip - modul pythona do instalowania bibliotek

def add(a,b):
    return a + b

# nazwa testu MUSI zawierac na poczatku 'test_'
# nastepnie POWINNA znajdowac sie nazwa testowanej funkcji
# nastepnie POWINNA pojawic sie informacja o pobieranych argumentach

def test_add_2_3():
    assert add(2,3) == 5

def test_add_for_strings():
    assert add('a', 'b') == 'ab'

def test_add_two_lists():
    assert add([1,2], ['a','b','c']) == [1, 2,'a','b','c']

# uruchamiamy piszac: pytest test.py

def return_absolute(n):
    if n >= 0:
        return n
    else:
        return -n

def test_return_absolute_positive():
    assert return_absolute(5) == 5

def test_return_absolute_negative():
    assert return_absolute(-5) == 5

def test_return_absolute_zero():
    assert return_absolute(0) == 0

def test_return_absolute_float():
    assert return_absolute(-1.234) == 1.234

# ex33
