# using / and *

def add_(a, b, /, *, c, d):
    print(a, b, c, d)

add_(1, 2, c=3, d=4)
add_(1, 2, 3, 4)
