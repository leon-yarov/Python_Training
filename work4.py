"""
Presenter: Leon Yarovinski, ID:206817181
"""


# ---1---
print("\n\n============= 1 ===============\n\n")

class Time(object):
    """
    Time class
    hour: int
    minute: int
    """
    hour, min = 0, 0

    def __init__(self, hour, min):
        self.hour = hour
        self.min = min

    def __str__(self):
        return '{:02d}:{:02d}'.format(int(self.hour), int(self.min))

    def __repr__(self):
        return 'Time({},{})'.format(int(self.hour), int(self.min))


class Event(object):
    """
    Event class
    time: Time class
    event: str
    """

    def __init__(self, time, event):
        self.time = time
        self.event = event

    def __str__(self):
        return '{} - {}'.format(self.time, self.event)

    def __repr__(self):
        return 'Event({},"{}")'.format(self.time.__repr__(), self.event)


class MedicalRecord(object):
    """
    MedicalRecord class
    name: str
    id: int
    """
    data = {}

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def __repr__(self):
        return 'MedicalRecord("{}",{},{})'.format(self.name, self.id, self.data)

    def add(self, time, event):
        """
        add event to the medical record
        time: time sting
        event: str
        """
        self.data[time] = Event(Time(*tuple(time.split(":"))), event)

    def view(self):
        """
        view medical record
        """
        print("name: ", self.name)
        print("ID: ", self.id)
        for key, value in sorted(self.data.items()): print(key, " - ", value.event)


time1=Time(8,2)
print(time1)
time2=eval(repr(time1))
print(time2)
event1=Event(time1,'registration')
print(event1)
Event(Time(8,2),'registration')
event2=eval(repr(event1))
print(event2)
record1=MedicalRecord('David',1)
record1.add('08:02','registration')
print(record1.data)
record1.add('09:15','doctor checkup')
record1.add('08:45','doctor checkup')
record1.add('09:00','procedure')
record1.add('11:00','doctor checkup')
record1.add('09:25','radiography')
record1.add('11:30','hospital discharge')
record1.add('10:30','blood test')
record1.view()
print(record1)

# ---2---
print("\n\n============= 2 ===============\n\n")


def make_class(attrs, base=None):
    """
    Shmyton make class
    """

    def get(name):
        """
        Get object from class
        name: string
        return: object
        """
        if name in attrs:
            return attrs[name]
        elif base:
            return base['get'](name)

    def set(name, value):
        """
        Set object in class
        name: string
        value: object
        """
        attrs[name] = value

    def new(*args):
        """
        Create new class instance
        """
        attrs = {}

        def get(name):
            """
            Get object from class or base
            name: string
            return: object
            """
            if name in attrs:
                return attrs[name]
            else:
                value = cls['get'](name)
                if callable(value):
                    return lambda *args: value(obj, *args)
                else:
                    return value

        def set(name, value):
            """
            Set object in class
            name: string
            value: object
            """
            attrs[name] = value

        obj = {'get': get, 'set': set}
        init = get('__init__')
        if init: init(*args)
        return obj

    cls = {'get': get, 'set': set, 'new': new}
    return cls


def make_time_class():
    """
    Shmyton Time class
    hour: int
    minute: int
    """

    def __init__(self, hour, min):
        self['set']('hours', hour)
        self['set']('minutes', min)

    def __str__(self):
        return '{:02d}:{:02d}'.format(int(self['get']('hours')), int(self['get']('minutes')))

    return make_class(locals())


def make_event_class():
    """
    Shmyton Event class
    time: Time class
    event: str
    """
    def __init__(self, time, event):
        self['set']('time', time)
        self['set']('event', event)

    def __str__(self):
        return '{} - {}'.format(self['get']('time')['get']('__str__')(), self['get']('event'))

    return make_class(locals())


def make_medical_record_class():
    """
    Shmyton MedicalRecord class
    name: str
    id: int
    """

    def __init__(self, name, id):
        self['set']('name', name)
        self['set']('id', id)
        self['set']('data', {})

    def add(self, time, event):
        """
        Add time and event
        time: Time
        event: event
        """
        self['get']('data')[time] = EventClass['new'](TimeClass['new'](*tuple(time.split(":"))), event)

    def view(self):
        """
        View all events in object
        """
        print("name: ", self['get']('name'))
        print("ID: ", self['get']('id'))
        for key, value in sorted(self['get']('data').items()): print(key, " - ", value['get']('event'))

    return make_class(locals())


# classes init
TimeClass = make_time_class()
EventClass = make_event_class()
MedicalRecordClass = make_medical_record_class()

time1=TimeClass['new'](8,2)
print(time1['get']('hours'))
print(time1['get']('__str__')())
event1=EventClass['new'](time1,'registration')
print(event1['get']('__str__')())
record1=MedicalRecordClass['new']('David',1)
record1['get']('add')('08:02','registration')
record1['get']('data')['08:02']['get']('__str__')()
print(record1)
record1['get']('add')('09:15','doctor checkup')
print(record1['get']('data'))
record1['get']('add')('08:45','doctor checkup')
record1['get']('add')('09:00','procedure')
record1['get']('add')('11:00','doctor checkup')
record1['get']('add')('09:25','radiography')
record1['get']('add')('10:30','blood test')
record1['get']('add')('11:30','hospital discharge')
record1['get']('view')()

# ---3---
print("\n\n============= 3 ===============\n\n")

def make_class_named(val, attrs, base=None):
    """
       Shmyton make class with a name
       val: string
       attrs: object
       base: inherit class
       """

    def get(param):
        """
        Get object from class
        param: string
        return: object
        """
        if param in attrs:
            return attrs[param]
        elif base:
            return base['get'](param)

    def set(name, value):
        """
        Set object in class
        name: string
        value: object
        """
        attrs[name] = value

    def info():
        """
        Get information about the class
        """
        if base: base['info']()
        methods = tuple(map(lambda x: x[0], (filter(lambda x: callable(x[1]), attrs.items()))))
        attributes = tuple((filter(lambda x: not callable(x[1]), attrs.items())))
        print("Class: ", cls['get']('name'))
        print("Methods: ")
        for m in methods: print(m)
        print("Attributes: ")
        for a, v in attributes: print(a, ": ", v)

    def new(*args):
        """
        Create new class instance
        """
        local_attrs = {}

        def get(name):
            """
                   Get object from class
                   name: string
                   return: object
                   """
            if name in local_attrs:
                return local_attrs[name]
            else:
                value = cls['get'](name)
                if callable(value):
                    return lambda *args: value(obj, *args)
                else:
                    return value

        def set(name, value):
            """
            Set object in class
            name: string
            value: object
            """
            local_attrs[name] = value

        def info():
            """
            Get information about the child class
            """
            cls['info']()
            for a, v in local_attrs.items(): print(a, ": ", v)

        obj = {'get': get, 'set': set, 'info': info}
        init = get('__init__')
        if init: init(*args)
        return obj

    cls = {'get': get, 'set': set, 'new': new, 'info': info}
    cls['set']('name', val)
    return cls


# provided with work 4.....

def make_account_class():
    def __init__(self, owner, ID):
        self['set']('owner', owner)
        self['set']('ID', ID)

    return make_class_named('Account', {'__init__': __init__, 'interest': 0.05})
Account = make_account_class()
def make_saving_account_class():
    interest = 0.075
    type_acc = 'saving'

    def strAccount(self):
        s = self['get']('name') + '(owner:' + self['get']('owner') + ',ID:' + str(self['get']('ID'))
        return s + ',interest:' + str(self['get']('interest')) + ')'

    return make_class_named('SaveAccount', locals(), base=Account)


SaveAccount = make_saving_account_class()

print(Account['get']('name'))
print(SaveAccount['get']('name'))
acc = SaveAccount['new']('Bob', 1)
print(acc['get']('name'))

Account['info']()
acc['info']()

print("\n\n============= 4 ===============\n\n")
# ---4---

class Centimeters(object):
    """
    Centimeters class
    """

    def __init__(self, value): self.cm = value

    def __add__(self, other): return self.cm + other.cm

    def __sub__(self, other): return self.cm - other.cm

    def __repr__(self): return f"Centimeters({self.cm})"


class Inches(object):
    """
    Inches class
    """

    def __init__(self, value): self.inch = value

    def __add__(self, other): return self.inch + other.inch

    def __sub__(self, other): return self.inch - other.inch

    def __repr__(self): return f"Inches({self.inch})"


class Feets(object):
    """
    Feets class
    """

    def __init__(self, value): self.ft = value

    def __add__(self, other): return self.ft + other.ft

    def __sub__(self, other): return self.ft - other.ft

    def __repr__(self): return f"Feet({self.ft})"


#all operations on ft and inches and centimeters

def add_cm(cm1, cm2):        return Centimeters(cm1.cm + cm2.cm)
def sub_cm(cm1, cm2):        return Centimeters(cm1.cm - cm2.cm)
def add_inch(inch1, inch2):  return Inches(inch1.inch + inch2.inch)
def sub_inch(inch1, inch2):  return Inches(inch1.inch - inch2.inch)
def add_ft(ft1, ft2):        return Feets(ft1.ft + ft2.ft)
def sub_ft(ft1, ft2):        return Feets(ft1.ft - ft2.ft)
def add_cm_inch(cm1, inch1): return Centimeters(cm1.cm + inch1.inch * 2.54)
def add_cm_ft(cm1, ft1):     return Centimeters(cm1.cm + ft1.ft * 30.48)
def add_ft_inch(ft1, inch1): return Feets(ft1.ft + inch1.inch / 12)
def add_ft_cm(ft1, cm1):     return Feets(ft1.ft + cm1.cm / 30.48)
def add_inch_cm(inch1, cm1): return Inches(inch1.inch + cm1.cm / 2.54)
def add_inch_ft(inch1, ft1): return Inches(inch1.inch + ft1.ft * 12)
def sub_cm_inch(cm1, inch1): return Centimeters(cm1.cm - inch1.inch * 2.54)
def sub_cm_ft(cm1, ft1):     return Centimeters(cm1.cm - ft1.ft * 30.48)
def sub_ft_inch(ft1, inch1): return Feets(ft1.ft - inch1.inch / 12)
def sub_ft_cm(ft1, cm1):     return Feets(ft1.ft - cm1.cm / 30.48)
def sub_inch_cm(inch1, cm1): return Inches(inch1.inch - cm1.cm / 2.54)
def sub_inch_ft(inch1, ft1): return Inches(inch1.inch - ft1.ft * 12)


def type_tag(x):
    """Return the tag associated with the type of x."""
    type_tag.tags = {Centimeters: 'cm', Feets: 'ft', Inches: 'inch'}
    return type_tag.tags[type(x)]


def apply(operator_name, x, y):
    """Get the correct function for the operator and apply it to x and y."""
    tags = (type_tag(x), type_tag(y))
    key = (operator_name, tags)
    return apply.implementations[key](x, y)


apply.implementations = {
    ('add', ('cm', 'cm')): add_cm,
    ('add', ('cm', 'inch')): add_cm_inch,
    ('add', ('cm', 'ft')): add_cm_ft,
    ('add', ('inch', 'cm')): add_inch_cm,
    ('add', ('inch', 'inch')): add_inch,
    ('add', ('inch', 'ft')): add_inch_ft,
    ('add', ('ft', 'cm')): add_ft_cm,
    ('add', ('ft', 'inch')): add_ft_inch,
    ('add', ('ft', 'ft')): add_ft,
    ('sub', ('cm', 'cm')): sub_cm,
    ('sub', ('cm', 'inch')): sub_cm_inch,
    ('sub', ('cm', 'ft')): sub_cm_ft,
    ('sub', ('inch', 'cm')): sub_inch_cm,
    ('sub', ('inch', 'inch')): sub_inch,
    ('sub', ('inch', 'ft')): sub_inch_ft,
    ('sub', ('ft', 'cm')): sub_ft_cm,
    ('sub', ('ft', 'inch')): sub_ft_inch,
    ('sub', ('ft', 'ft')): sub_ft,
}
print(apply('add',Inches(1),Centimeters(150)))
print(apply('add',Centimeters(100),Feets(1.5)))
print(apply('add',Feets(2),Inches(5)))
print(apply('sub',Inches(1.5),Centimeters(100)))
print(apply('sub',Feets(2),Inches(5)))
print(apply('sub',Centimeters(100),Inches(15)))

# ---- 5 -----

print("\n\n============= 5 ===============\n\n")

def cm_to_feet(cm): return Feets(cm.cm / 30.48)
def cm_to_inch(cm): return Inches(cm.cm / 2.54)
def feet_to_cm(ft): return Centimeters(ft.ft * 30.48)
def feet_to_inch(ft): return Inches(ft.ft * 12)
def inch_to_cm(inch): return Centimeters(inch.inch * 2.54)
def inch_to_feet(inch): return Feets(inch.inch / 12)


coercions = {
    ('ft', 'cm'): feet_to_cm,
    ('ft', 'inch'): feet_to_inch,
    ('cm', 'ft'): cm_to_feet,
    ('cm', 'inch'): cm_to_inch,
    ('inch', 'cm'): inch_to_cm,
    ('inch', 'ft'): inch_to_feet
}


def coerce_apply(operator_name, x, y):
    """Apply the operator to x and y by conversion"""
    tx, ty = type_tag(x), type_tag(y)
    if tx != ty:
        if (tx, ty) in coercions:
            tx, x = ty, coercions[(tx, ty)](x)
        elif (ty, tx) in coercions:
            ty, y = tx, coercions[(ty, tx)](y)
        else:
            return 'No coercion possible.'
    assert tx == ty
    key = (operator_name, tx)
    return coerce_apply.implementations[key](x, y)


coerce_apply.implementations = {
    ('add', 'cm'): add_cm,
    ('add', 'inch'): add_inch,
    ('add', 'ft'): add_ft,
    ('sub', 'cm'): sub_cm,
    ('sub', 'inch'): sub_inch,
    ('sub', 'ft'): sub_ft
}


print(coerce_apply('add',Inches(1),Centimeters(150)))
print(coerce_apply('add',Centimeters(100),Feets(1.5)))
print(coerce_apply('add',Feets(2),Inches(5)))
print(coerce_apply('sub',Inches(1.5),Centimeters(100)))
print(coerce_apply('sub',Feets(2),Inches(5)))
print(coerce_apply('sub',Centimeters(100),Inches(15)))
# ---- 6 ----
print("\n\n============= 6 ===============\n\n")

def make_medical_Record(name, d):
    '''
    Return a medical record dictionary
    name: string
    d: number
    '''
    try:
        if type(name) is not str or type(d) is not int: raise TypeError("Incorrect parameter type")
    except TypeError as e:
        print(e)
        print("ID:", type(d))
        print("name:", type(name))

    data = {}

    def addData(time, what):
        '''
        Add data to the medical record
        time: number
        what: string
        '''
        try:
            if len(time) != 5: raise ValueError("Incorrect time format: ")
        except ValueError as e:
            print(e)
            print("time:", time)
            return

        try:
            t = time.split(':')
            if 0 > int(t[0]) or int(t[0]) >= 24 or 0 > int(t[1]) or int(t[1]) >= 60: raise ValueError(f"Incorrect time:")
        except ValueError as e:
            print(e)
            print("time:", time)
            return

        try:
            if what in data.values(): raise ValueError(f"This event is present")
        except ValueError as e:
            print(e)
            print("event:", what)
        else:
            data[time] = what

    def inData(what):
        '''
        Return True if what is in the medical record
        what: string
        '''
        return what in data.values()

    def notInData(what):
        '''
        Return True if what is not in the medical record
        what: string
        '''
        return not inData(what)

    def view(what):
        '''
        Return the time of what
        what: string
        '''
        w = [k for k in data if data[k] == what]
        if len(w) > 0:
            print(sorted(w))
        else:
            print("No Events")

    def printRecord(iter=0):
        '''
        Print the medical record
        iter: number
        '''
        print(f'{name} {d}')

        def next():
            '''
            Print the next event
            '''
            nonlocal iter
            try:
                if iter >= len(data): raise IndexError("list index out of range")
            except IndexError as e:
                print(e)
            else:
                items = list(sorted(data.items()))
                print(f'{items[iter][0]}-{items[iter][1]}')
                iter += 1

        def hasMore():
            '''
            Return True if there are more events
            '''
            nonlocal iter
            if iter == len(data): return False
            return True

        return {"next": next, "hasMore": hasMore}

    return {'addData': addData, 'notInData': notInData, 'inData': inData, 'view': view, 'printRecord': printRecord}


mr = make_medical_Record(1,'David')
mr = make_medical_Record('David', 1)
mr['addData']('11:30:20','registration')
mr['addData']('11:3','registration')
mr['addData']('11:62','registration')
mr['addData']('11:30','registration')
mr['addData']('11:40','registration')
mr['addData']('11:40','abcd')
mr['addData']('12:50','doctor checkup')
mr['addData']('11:40','doctor checkup')
mr['addData']('12:40','procedure')
mr['addData']('13:30','radiography')
mr['addData']('13:40','blood test')
mr['addData']('15:00','hospital discharge')
pr=mr['printRecord']()
pr['next']()
for _ in range(8):
    pr['next']()

# ------ 7 ------
print("\n\n============= 7 ===============\n\n")

class Tree():
    """Binary tree implementation"""
    def __init__(self, entry, left=None, right=None):
        self.entry = entry
        self.left = left
        self.right = right

    def __repr__(self):
        if not self.left and not self.right:
            return "Tree({0})".format(repr(self.entry))
        return "Tree({0},{1},{2})".format(repr(self.entry), repr(self.left), repr(self.right))


def build_tree(tree):
    """Build tree from given list"""
    if len(tree) == 1:
        return Tree(tree[0])
    return Tree(tree[0], build_tree(tree[1]), build_tree(tree[2]))


def max_tree(tree):
    """Get the max element in a tree"""
    if tree.left is None and tree.right is None: return tree.entry
    return max(tree.entry, max_tree(tree.left), max_tree(tree.right))


def min_tree(tree):
    """Get the max element in a tree"""
    if tree.left is None and tree.right is None: return tree.entry
    return min(tree.entry, min_tree(tree.left), min_tree(tree.right))


def is_BST_tree(tree):
    """Check if a tree is a BST
    tree: a binary tree"""
    return True if max_tree(tree.left) < tree.entry and min_tree(tree.right) > tree.entry else False


tree1 = (12, (6, (2,), (8,)), (15, (14,), (18,)))
t1 = build_tree(tree1)
print(t1)
tree2 = (12, (6, (2,), (8,)), (15, (7,), (20,)))
t2=build_tree(tree2)
print(t2)
print(max_tree(t1))
print(min_tree(t2))
print(is_BST_tree(t1))
print(is_BST_tree(t2))

# ------ 8 ------
print("\n\n============= 8 ===============\n\n")
print("...Test with interpreter...")
print("Launch the 'read_eval_print_loop()' function")
class Exp(object):
    """Expression class"""
    def __init__(self, op, operands): self.operator, self.operands = op, operands
    def __repr__(self): return f'Exp({repr(self.operator)},{repr(self.operands)})'
    def __str__(self):  return f'{self.operator}({",".join(map(str, self.operands))})'


from operator import mul
from functools import reduce


def calc_apply(operator, args):
    """Calculate the result of an expression"""
    if operator in ('add', '+'): return sum(args)

    if operator in ('sub', '-'):
        if len(args) == 0: raise TypeError(operator + ' required at least 1 argument')
        if len(args) == 1: return -args[0]
        return sum(args[0] + [-arg for arg in args[1:]])

    if operator in ("mul", '*'): return reduce(mul, args, 1)

    if operator in ('dev', '/'):
        if len(args) != 2: raise TypeError(operator + ' requires exactly 2 arguments')
        return args[0] / args[1]

    if operator in ('V', 'sqrt'):
        if len(args) != 1: raise TypeError(operator + ' requires exactly 1 arguments')
        return args[0] ** 0.5

    if operator in ('round', '~'):
        if len(args) != 2: raise TypeError(operator + ' requires exactly 2 arguments')
        if type(args[0]) is int: raise TypeError('You can round only floats')
        return round(args[0], args[1])

    if operator in ('&', 'weight'):
        if type(args[0]) is not int or len(args) > 1: raise TypeError('You can weight only single int')
        return int(''.join(map(lambda n: str(10 - int(n)), filter(lambda n: n != '0', list(str(args[0]))))))


def calc_eval(exp):
    """Evaluate an expression"""
    if type(exp) in (int, float):
        return exp
    elif type(exp) == Exp:
        return calc_apply(exp.operator, list(map(calc_eval, exp.operands)))


def tokenize(line):
    """Tokenize a line"""
    return line.replace('(', ' ( ').replace(')', ' ) ').replace(',', ' , ').split()


def assert_non_empty(tokens):
    """Assert that the tokens are not empty"""
    if len(tokens) == 0: raise SyntaxError('unexpected end of line')


def analyze_operands(tokens):
    """Analyze all operands"""
    assert_non_empty(tokens)
    operands = []
    while tokens[0] != ')':
        if operands and tokens.pop(0) != ',':
            raise SyntaxError('expected: ,')
        operands.append(analyze(tokens))
        assert_non_empty(tokens)
    tokens.pop(0)
    return operands


def analyze_token(token):
    """Analyze a token for correctness"""
    try:
        return int(token)
    except (TypeError, ValueError):
        try:
            return float(token)
        except (TypeError, ValueError):
            return token


def analyze(tokens):
    """
    Analyze all tokens
    tokens: a list of tokens
    return: Exp object or single value
    """
    ops = ['add', 'sub', 'mul', 'div', '+', '-', '/', '*'] + ['round', '~', 'V', 'sqrt', '&', 'weight']
    assert_non_empty(tokens)
    token = analyze_token(tokens.pop(0))
    if type(token) in (int, float):
        return token
    if token in ops:
        if len(tokens) == 0 or tokens.pop(0) != '(':
            raise SyntaxError('expected ( after ' + token)
        return Exp(token, analyze_operands(tokens))
    else:
        raise SyntaxError('unexpected token: ' + token)


def calc_parse(line):
    """
    Parse a line and return a tree
    line: string
    """
    tokens = tokenize(line)
    exo_tree = analyze(tokens)
    if len(tokens) > 0:
        raise SyntaxError('Extra token(s): ' + ' '.join(tokens))
    return exo_tree


def read_eval_print_loop():
    """
    Calc loop to extend the interpreter
    """
    while True:
        try:
            exp_tree = calc_parse(input('calc> '))
            print(calc_eval(exp_tree))
        except (SyntaxError, TypeError, ZeroDivisionError) as err:
            print(type(err).__name__ + ':', err)
        except (KeyboardInterrupt, EOFError):  # <Control>-D, etc. <ctrl-C>
            print('Calculation completed.')
            return
