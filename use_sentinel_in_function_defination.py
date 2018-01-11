'''
use a placeholder value to prevent the returned value changed in multiple function calls
'''
sentinel = object()

def foo(a=sentinel):
    if a is sentinel:
        a = []
    a.append(5)
    return a

print(foo())
print(foo())
print(foo())

