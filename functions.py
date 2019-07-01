def say_hello():
    print("Hello")

def say_hello_to_someone(name):
    print(f"Hello {name}")


# say_hello()
# say_hello_to_someone("Tomek")
# say_hello_to_someone("Anna")
# say_hello_to_someone("R2D2")
# say_hello_to_someone(5)
# say_hello_to_someone([1,2,3])

def check_suspect(police_docs, suspect):
    print("***")
    for item in police_docs:
        if item in suspect.keys():
            print(f"{item} -> {suspect[item]}")
        else:
            print(f"{item} -> brak danych")


suspect1 = {'name':'Anna', 'surname':'Nowak', 'occupation':'actress'}
suspect2 = {'occupation':'developer', 'age': 30, 'friends':None}
suspect3 = {'name':'Jan', 'surname':'Kowalski', 'occupation':'medic',\
 'age': 40, 'friends': ["Anna", "Zosia", "Kasia"]}
police_req = ['name', 'surname', 'age', 'occupation', 'friends']
police_req2 = ['name', 'surname', 'age']
#
check_suspect(police_req2, suspect2)
check_suspect(police_req, suspect3)
check_suspect(police_req2, suspect3)
#
#
# docstrings
def f1():
    '''Ta funkcja bedzie
    cos madrego robic'''
    pass # jesli jednak nie chce nam sie jej pisac

print(f1.__doc__)  # tak drukujemy docstringi

# # ex27
