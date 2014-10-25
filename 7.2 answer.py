__author__ = 'Alicia'


def world(x="Hello"):
    return x + " " + 'World'


def add(m=1, n=1):
    sum = 0
    for i in range(m, n+1):
        sum += i
    return sum


def box(m, n=None):
    if n is None:
        n = m
        y = "+" + m*"-" + "+"
        x = "|" + m*" " + "|" + '\n'
        return y + '\n' + n*x + y + '\n'
    else:
        y = "+" + m*"-" + "+"
        x = "|" + m*" " + "|" + '\n'
        return y + '\n' + n*x + y + '\n'


print(world())
print(world("Time to take over the"))
print(world("I Rule the"))
print(add())
print(add(n=10))
print(add(20, 30))
print(add(6, 20))
print(box(4))
print(box(4, 6))
print(box(10, 5))
print(box(7))