def text_preprocessing(text,stopwords):
    filtered = tuple(filter(lambda x: x not in stopwords and not x.isnumeric(), map (lambda x: x.lower(), text.split())))
    return {x: list(filtered).count(x) for x in set(filtered)}

stop_list = ('is', 'it', 'a', 'the', 'my', 'and')

print (text_preprocessing ('My cat is 10 and it is a very fat cat', stop_list))

def make_account(money = 0):
    def dispatch(n):
        def charge(v):
            nonlocal money
            if v > 0:
                money += v
            elif money - abs(v) > 0:
                money -= abs(v)
            else:
                return 'out of funds'
            return money
        def move(a,m):
            nonlocal money
            if (m < 0):
                return 'Negative transaction'
            if charge(-m) == 'out of funds':
                return 'No money for transactions'
            a('change')(m)
            return (money,a('get'))
        if n == 'get':
            return money
        if n == 'change':
            return charge
        if n == 'move':
            return move
    return dispatch

a1 = make_account()
print(a1)
a2 = make_account()
print(a1('change')(20))
print(a1('get'))
print(a1('change')(-25))
print(a1('move')(a2, 7))
print(a2('move')(a1, 2))
print(a1('move')(a2, 30))
print(a1('move')(a2, -30))


make_pairs = lambda el,lst: tuple(map(lambda x: (el,x),lst))
print(make_pairs(5, (1,2,3)))

c_prod = lambda lst1, lst2: tuple(map(lambda x: make_pairs(x,lst2),lst1))
print(c_prod((1, 2), (3, 4)) )

