def make_circle(x,y,radius): # Immutable type
    def dispatch(m):
        if m == 0:
            return x
        elif m == 1:
            return y
        elif m == 2:
            return radius
    return dispatch


def x(circle):
    return circle(0)


def y(circle):
    return circle(1)


def radius(circle):
    return circle(2)


def print_circle(circle):
    print(f'X: {x(circle)}' ,f'Y: {y(circle)}',f'Radius: {radius(circle)}')


def perimeter(circle):
    return 2 * 3.1415926 * radius(circle)


def area(circle):
    return 3.1415926 * radius(circle) ** 2


def distance(c1,c2):
    return ((x(c1)-x(c2))**2 + (y(c1)-y(c2))**2)**0.5


def replace(circle,x,y):
    return make_circle(x,y,radius(circle))


def set_radius(circle,new_radius):
    return make_circle(x(circle),y(circle),new_radius)


def add(c1,c2):
    return make_circle((x(c1) + x(c2))//2, (y(c1) + y(c2))//2, radius(c1)+radius(c2))


def make_date(d,m,y):
    def dispatch(n):
        if n == 0:
            return d
        elif n == 1:
            return m
        elif n == 2:
            return y
    return dispatch

d = make_date(23,6,2021)

def day(date):
    return date(0)


def month(date):
    return date(1)


def year(date):
    return date(2)


def print_date(date, format):
    if date is None: return
    if format == 'dmy':
        print(f'{day(date)}/{month(date)}/{year(date)}')
    elif format == 'mdy':
        print(f'{month(date)}/{day(date)}/{year(date)}')
    elif format == 'ymd':
        print(f'{year(date)}/{month(date)}/{day(date)}')
    else:
        return 'Error format'


def next_date(date):
    d,m,y = day(date),month(date),year(date)
    days_per_month = 30 if month(date) in [4,6,9,11] else 28 if month(date) == 2 else 31
    if d >= days_per_month:
        d = 1
        if m == 12: m,y = 1, y + 1
        else: m+= 1
    else : d += 1
    return make_date(d,m,y)


def set_day(date, new_day):
    days_per_month = 30 if month(date) in [4, 6, 9, 11] else 28 if month(date) == 2 else 31
    if day(date) < 1:
        print('Error')
        return None
    if new_day > days_per_month:
        return make_date(days_per_month,month(date),year(date))
    return make_date(new_day,month(date),year(date))


def set_month(date,new_month):
    if new_month == 2 and day(date) > 28 or 12 < new_month < 0:
        print("Day-Month invalid")
        return None
    return make_date(day(date),new_month,year(date))


def set_year(date,new_year):
    if 1900 < new_year < 2050:
        return make_date(day(date),month(date),new_year)
    print('Error year')
    return None


def diff(d1,d2):
    if year(d1) == year(d2) and month(d1) == month(d2):
        return abs(day(d1) - day(d2))
    return -1


def convert(grades):
    return tuple(filter(lambda x: len(x[1]) != 0, {
        'A': list(filter(lambda x: 90 < x < 101, grades)),
        'B': list(filter(lambda x: 80 < x < 91, grades)),
        'C': list(filter(lambda x: 70 < x < 81, grades)),
        'D': list(filter(lambda x: 55 < x < 71, grades)),
        'Fail': list(filter(lambda x: 0 <= x < 56, grades))
    }.items()))


lst = (20, 45, 90, 3, 68, -30, 81, 98, 104, 63, 61)
print(convert(lst))

def fact(grades,factor):
    g = tuple(map(lambda x: tuple(map(lambda y: y*factor if y*factor <= 100 else 100, x)), grades))
    return tuple(zip(list(map(min,g)),list(map(max,g)),list(map(lambda x: sum(x)/len(x),g))))


lst = ((30, 80, 72, 40), (24,), (88, 50, 34, 90, 56))
print(fact(lst,1.5))


def make_currency(amount,sign):
    def dispatch(n):
        def set(n,v):
            nonlocal amount, sign
            if n == 'amount':   amount = v
            elif n == 'symbol': sign = v
        def get(n):
            if n == 'amount':   return amount
            elif n == 'symbol': return sign
        def convert(f,s):
            nonlocal sign, amount
            set('amount',f(amount))
            set('symbol',s)
        if n == 'get_value':
            return get
        elif n == 'set_value':
            return set
        elif n == 'str':
            return f'{sign}{amount}'
        elif n == 'convert':
            return convert
    return dispatch

c = make_currency(10.50, '$')
print(c('get_value')('amount'))
print(c('get_value')('symbol'))
c('set_value')('amount',50)
print(c('get_value')('amount'))
print(c('str'))
c('convert')(lambda x: x*3.87,'€')
print(c('str'))


def make_medical_Record(name,d):
    data = {}
    def addData(time,what):
        data[time] = what
    def inData(what):
        return what in data.values()
    def notInData(what):
        return not inData(what)
    def view(what):
        w = [k for k in data if data[k] == what]
        if len(w) > 0:
            print(sorted(w))
        else: print("No Events")
    def printRecord(iter = 0):
        print(f'{name} {d}')
        def next():
            nonlocal iter
            items = list(sorted(data.items()))
            print(f'{items[iter][0]}-{items[iter][1]}')
            iter += 1
        def hasMore():
            nonlocal iter
            if iter == len(data) : return False
            return True
        return {"next":next, "hasMore": hasMore}
    return {'addData': addData,'notInData' :notInData,'inData': inData,'view': view,'printRecord': printRecord}

mr=make_medical_Record('David',1)
print(mr)
mr['addData']('11:30','registration')
print(mr['inData']('registration'))
print(mr['inData']('procedure'))
print(mr['notInData']('procedure'))
mr['addData']('12:50','doctor checkup')
mr['addData']('11:40','doctor checkup')
mr['addData']('12:40','procedure')
mr['addData']('14:30','doctor checkup')
mr['addData']('13:30','radiography')
mr['addData']('13:40','blood test')
mr['view']('doctor checkup')
mr['view']('hospital discharge')
mr['addData']('15:00','hospital discharge')
pr=mr['printRecord']()
print(pr)
pr['next']()
while pr['hasMore']():
	pr['next']()






