from functools import reduce


def accumulate(first, function, array):
    for element in array:
        first = function(first, element)
    return first


print(accumulate(1, lambda x, y: 4 * x - y, [1, 2, 3, 4, 5]))


def mymap(function, array):
    return [function(element) for element in array]


print(tuple(mymap(lambda x: x ** 2, [1, 2, 3, 4, 5])))


def orfilter(func1, func2):
    return lambda x: func1(x) or func2(x)


# print(tuple(orfilter(lambda x: x % 2 == 0, lambda x: x % 3 == 0, range(20))))


def iseven(x):
    return x % 2 == 0


def issquare(x):
    return int(x ** 0.5) ** 2 == x


# tests
print(list(filter(orfilter(iseven, issquare), range(20))))
# [0, 1, 2, 4, 6, 8, 9, 10, 12, 14, 16, 18]
print(list(filter(accumulate(lambda x: False, orfilter, (iseven, issquare)), range(20))))
# [0, 1, 2, 4, 6, 8, 9, 10, 12, 14, 16, 18]
print(list(filter(mymap(lambda f: orfilter(f, issquare), (iseven,))[0], range(20))))
# [0, 1, 2, 4, 6, 8, 9, 10, 12, 14, 16, 18]
print(list(filter(mymap(lambda f: orfilter(f, issquare), (iseven,))[0], range(20))))


def average_passed_grade(grades):
    def f(x): return 10 * (x ** 0.5)

    s = [f(x) for x in grades if f(x) >= 56 and x != 199]
    return sum(s) / len(s)


print(average_passed_grade([23, 64, 199, 20, 77, 98, 100, 199]))


def average_passed_grade2(grades, function):
    s = [function(x) if function(x) < 100 else 100 for x in grades if function(x) >= 56 and x != 199]
    return sum(s) / len(s)


print(average_passed_grade2([23, 64, 199, 20, 77, 98, 100, 199], lambda x: x + 15))
