def trapezoid(f,a,b,n):
    '''
    Returns the integral of f from a to b using n trapezoids
    :param f: function of x
    :param a: lower bound
    :param b: upper bound
    :param n: number of trapezoids
    :return: integral of f from a to b
    '''
    h, s = (b-a)/n, f(a) + f(b)  # h is the width of the trapezoid, s is the sum of the function values
    for i in range(1,n):
        s += 2*f(a+i*h)     # summation of the function values
    return s*h/2


def myFilter(lst,func):
    '''
    Returns a list of elements in lst that satisfy func
    :param lst: list of elements
    :param func: lambda function of any bool function
    :return: list of elements in lst that satisfy func
    '''
    return [x for x in lst if func(x)]


def myFilterMulti(lst, funcL):
    '''
    Returns a list of elements in lst that satisfy list of functions
    :param lst: list of elements
    :param funcL: list of functions
    :return: list of elements in lst that satisfy list of functions
    '''
    # check if x satisfies all functions in funcL
    def check(funcs, x):
        for f in funcs:
            if not f(x):
                return False
        return True
    return [x for x in lst if check(funcL, x)]

def myPrime(x):
    '''
    check if x is a prime number
    :param x: number for the test
    :return: True if x is a prime number
    '''
    return [i for i in range(2,x) if x%i == 0] == []    # check if x is divisible by any number between 2 and x-1


def isFib(x):
    '''
    check if x is a Fibonacci number
    :param x: number for the test
    :return: bolean if x is a Fibonacci number
    '''
    def perfectSquare(x): # check if x is a perfect square
        return int(x**0.5)**2 == x
    return perfectSquare(5*(x**2) + 4) or perfectSquare(5*(x**2) - 4)   # check is Binets part of the formula is true

# myFilerMulti test
print(myFilterMulti([2,4,5,6,7,13,56,89,100,107,144],[lambda x: x > 9 and x < 100, myPrime, isFib]))

