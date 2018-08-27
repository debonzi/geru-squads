

def set_family(func):
    def wrapper():
        return func() + ' Debonzi'
    return wrapper

@set_family
def my_name():
    return 'Daniel'


print(my_name())