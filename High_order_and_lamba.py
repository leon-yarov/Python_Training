import math

F = lambda x: x +2
F = lambda x: x*x+3*x-2
F = lambda x,y: (x+y)/(x-y)


def intergral(f,a,b):
    total,k = 0,0
    delta = (b-a)/100
    while k <= 99:
        total, k = total + f(a + delta*k)*delta, k + 1
    return total

# print(intergral(lambda x: x**2, 0, 1))

def derivative(f):
    delta = 0.0001
    def tag(x):
        return (f(x+delta) -f(x)) / delta
    return tag

# print(derivative(lambda x:x**2)(3))
# print(derivative(math.sin)(math.pi))

def sec_der(f):
    return derivative(derivative(f))


# print(sec_der(lambda x:x**2)(3))


def partial_der_x(f):
    delta = 0.001
    def tag(x,y):
        return (f(x + delta,y) - f(x,y)) / delta
    return tag

# print(partial_der_x(lambda x,y: x* (y**2) - 2*x*y)(2,3))


def partial_der_y(f):
    delta = 0.001
    def tag(x,y):
        return (f(x,y + delta) - f(x,y)) / delta
    return tag
# print(partial_der_y(lambda x,y: x* (y**2) - 2*x*y)(2,3))

def like_fib(f):
    def g(n):
        return f(n-2) + f(n-1)
    return g

# print(like_fib(lambda x: 5 -x)(3))

def smooth(f):
    def g(n):
        return (f(n-1) + f(n) + f(n+1))/3
    return g

print(smooth(lambda x: 5-x)(2))
