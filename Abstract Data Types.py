def add_complex(c1,c2):
    return real(c1) + real(c2), imag(c1) + imag(c2)


def abs_complex(c):
    return (real(c)**2 + imag(c)**2)**0.5


def str_complex(c):
    return "({}+{}i)".format(real(c), imag(c))


def make_complex(a, b):
    return a, b


def real(c):
    return c[0]


def imag(c):
    return c[1]

# c = make_complex(2,3)
# print(str_complex(c))
# print(str_complex(add_complex(c,c)))
# print(abs_complex(c))


def make_complex(a,b):
    def dispatch(x):
        if x==0: return a
        elif x==1: return b
    return dispatch


def real(c):
    return c(0)


def imag(c):
    return c(1)


def str_complex(c):
    return "{}+{}i".format(real(c),imag(c))


# c = make_complex(2,3)
# print(str_complex(c))

empty_rlist = None
def make_rlist(first,rest):
    return first,rest

def first(l):
    return l[0]

def rest(l):
    return l[1]

def len_rlist(l):
    if l is None : return 0
    return 1+len_rlist(rest(l))

def print_rlist(l):
    while l is not None:
        print(first(l), end=', ')
        l = rest(l)

counts=make_rlist(1,make_rlist(2,make_rlist(3,make_rlist(4,None))))

def reverse_rlist(l):
    c = make_rlist(first(l),None)
    while rest(l) is not None:
        l = rest(l)
        c = make_rlist(first(l),c)
    return c

print_rlist(reverse_rlist(counts))

