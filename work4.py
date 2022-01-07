"""
Presenter: Leon Yarovinski 206817181
"""


# ---1---

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


# ---2---


def make_class(attrs, base=None):
    def get(name):
        if name in attrs:
            return attrs[name]
        elif base:
            return base['get'](name)

    def set(name, value):
        attrs[name] = value

    def new(*args):
        attrs = {}
        def get(name):
            if name in attrs:
                return attrs[name]
            else:
                value = cls['get'](name)
                if callable(value): return lambda *args: value(obj, *args)
                else: return value

        def set(name, value):
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
        self['get']('data')[time] = EventClass['new'](TimeClass['new'](*tuple(time.split(":"))), event)

    def view(self):
        print("name: ", self['get']('name'))
        print("ID: ", self['get']('id'))
        for key, value in sorted(self['get']('data').items()): print(key, " - ", value['get']('event'))

    return make_class(locals())

#classes init
TimeClass = make_time_class()
EventClass = make_event_class()
MedicalRecordClass = make_medical_record_class()



# ---3---

def make_class_named(val,attrs, base=None):
    def get(param):
        if param in attrs:
            return attrs[param]
        elif base:
            return base['get'](param)

    def set(name, value):
        attrs[name] = value

    def info():
        if base: base['info']()
        methods = tuple(map(lambda x: x[0],(filter(lambda x: callable(x[1]), attrs.items()))))
        attributes = tuple((filter(lambda x: not callable(x[1]), attrs.items())))
        print("Class: ", cls['get']('name'))
        print("Methods: ")
        for m in methods: print(m)
        print("Attributes: ")
        for a,v in attributes: print(a, ": ", v)


    def new(*args):
        local_attrs = {}
        def get(name):
            if name in local_attrs:
                return local_attrs[name]
            else:
                value = cls['get'](name)
                if callable(value): return lambda *args: value(obj, *args)
                else: return value
        def set(name, value):
            local_attrs[name] = value

        def info():
            cls['info']()
            for a,v in local_attrs.items(): print(a, ": ", v)

        obj = {'get': get, 'set': set,'info': info}
        init = get('__init__')
        if init: init(*args)
        return obj

    cls = {'get': get, 'set': set, 'new': new, 'info': info}
    cls['set']('name', val)
    return cls

def make_account_class():
    def __init__(self, owner, ID):
        self['set']('owner', owner)
        self['set']('ID', ID)
    return make_class_named('Account',{ '__init__' : __init__ , 'interest' : 0.05})

Account = make_account_class()

def make_saving_account_class():
    interest=0.075
    type_acc='saving'
    def strAccount(self):
        s=self['get']('name')+'(owner:'+self['get']('owner')+',ID:'+str(self['get']('ID'))
        return s+',interest:'+ str(self['get']('interest'))+')'
    return make_class_named('SaveAccount',locals(), base=Account)

SaveAccount = make_saving_account_class()
acc=SaveAccount['new']('Bob',1)

# ---4---

class Centimeters(object):
    def __init__(self, value): self.cm = value
    def __add__(self, other): return self.cm + other.cm
    def __sub__(self, other): return self.cm - other.cm
    def __repr__(self): return f"Centimeters({self.cm})"

class Inches(object):
    def __init__(self, value): self.inch = value
    def __add__(self, other):return self.inch + other.inch
    def __sub__(self, other):return self.inch - other.inch
    def __repr__(self): return f"Inches({self.inch})"

class Feets(object):
    def __init__(self, value): self.ft = value
    def __add__(self, other):return self.ft + other.ft
    def __sub__(self, other):return self.ft - other.ft
    def __repr__(self): return f"Feet({self.ft})"


def add_cm(cm1,cm2):        return Centimeters(cm1.cm + cm2.cm)
def sub_cm(cm1,cm2):        return Centimeters(cm1.cm - cm2.cm)
def add_inch(inch1,inch2):  return Inches(inch1.inch + inch2.inch)
def sub_inch(inch1,inch2):  return Inches(inch1.inch - inch2.inch)
def add_ft(ft1,ft2):        return Feets(ft1.ft + ft2.ft)
def sub_ft(ft1,ft2):        return Feets(ft1.ft - ft2.ft)
def add_cm_inch(cm1,inch1): return Centimeters(cm1.cm + inch1.inch*2.54)
def add_cm_ft(cm1,ft1):     return Centimeters(cm1.cm + ft1.ft*30.48)
def add_ft_inch(ft1,inch1): return Feets(ft1.ft + inch1.inch / 12)
def add_ft_cm(ft1,cm1):     return Feets(ft1.ft + cm1.cm / 30.48)
def add_inch_cm(inch1,cm1): return Inches(inch1.inch + cm1.cm/2.54)
def add_inch_ft(inch1,ft1): return Inches(inch1.inch + ft1.ft*12)
def sub_cm_inch(cm1,inch1): return Centimeters(cm1.cm - inch1.inch*2.54)
def sub_cm_ft(cm1,ft1):     return Centimeters(cm1.cm - ft1.ft*30.48)
def sub_ft_inch(ft1,inch1): return Feets(ft1.ft - inch1.inch / 12)
def sub_ft_cm(ft1,cm1):     return Feets(ft1.ft - cm1.cm / 30.48)
def sub_inch_cm(inch1,cm1): return Inches(inch1.inch - cm1.cm/2.54)
def sub_inch_ft(inch1,ft1): return Inches(inch1.inch - ft1.ft*12)

def type_tag(x):
    type_tag.tags = {Centimeters: 'cm', Feets: 'ft', Inches: 'inch'}
    """Return the tag associated with the type of x."""
    return type_tag.tags[type(x)]

def apply(operator_name, x, y):
    tags = (type_tag(x), type_tag(y))
    key = (operator_name, tags)
    return apply.implementations[key](x, y)

apply.implementations = {
    ('add', ('cm', 'cm')):      add_cm,
    ('add', ('cm', 'inch')):    add_cm_inch,
    ('add', ('cm', 'ft')):      add_cm_ft,
    ('add', ('inch', 'cm')):    add_inch_cm,
    ('add', ('inch', 'inch')):  add_inch,
    ('add', ('inch', 'ft')):    add_inch_ft,
    ('add', ('ft', 'cm')):      add_ft_cm,
    ('add', ('ft', 'inch')):    add_ft_inch,
    ('add', ('ft', 'ft')):      add_ft,
    ('sub', ('cm', 'cm')):      sub_cm,
    ('sub', ('cm', 'inch')):    sub_cm_inch,
    ('sub', ('cm', 'ft')):      sub_cm_ft,
    ('sub', ('inch', 'cm')):    sub_inch_cm,
    ('sub', ('inch', 'inch')):  sub_inch,
    ('sub', ('inch', 'ft')):    sub_inch_ft,
    ('sub', ('ft', 'cm')):      sub_ft_cm,
    ('sub', ('ft', 'inch')):    sub_ft_inch,
    ('sub', ('ft', 'ft')):      sub_ft,
}


def cm_to_feet(cm): return Feets(cm.cm / 30.48)
def cm_to_inch(cm): return Inches(cm.cm / 2.54)
def feet_to_cm(ft): return Centimeters(ft.ft * 30.48)
def feet_to_inch(ft): return Inches(ft.ft * 12)
def inch_to_cm(inch):return Centimeters(inch.inch * 2.54)
def inch_to_feet(inch):return Feets(inch.inch / 12)

coercions = {
    ('ft', 'cm'): feet_to_cm,
    ('ft', 'inch'): feet_to_inch,
    ('cm', 'ft'): cm_to_feet,
    ('cm', 'inch'): cm_to_inch,
    ('inch', 'cm'): inch_to_cm,
    ('inch', 'ft'): inch_to_feet
}

def coerce_apply(operator_name, x, y):
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

coerce_apply.implementations ={
    ('add', 'cm'): add_cm,
    ('add', 'inch'): add_inch,
    ('add', 'ft'): add_ft,
    ('sub','cm'): sub_cm,
    ('sub','inch'): sub_inch,
    ('sub','ft'): sub_ft
}



def make_medical_Record(name,d):
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
    def addData(time,what):
        '''
        Add data to the medical record
        time: number
        what: string
        '''
        try:
            if len(time) != 5: raise ValueError("Incorrect time format")
        except ValueError as e:
            print(e)
            print("time:", time)
            return

        try:
            t = time.split(':')
            if  0 > int(t[0]) or int(t[0]) >= 24 or 0 > int(t[1]) or int(t[1])>= 60: raise ValueError("Incorrect time")
        except ValueError as e:
            print(e)
            print("time:", time)
            return

        try:
            if what in data.values(): raise ValueError("This event is present")
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
        else: print("No Events")
    def printRecord(iter = 0):
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
            if iter == len(data) : return False
            return True
        return {"next":next, "hasMore": hasMore}
    return {'addData': addData,'notInData' :notInData,'inData': inData,'view': view,'printRecord': printRecord}



mr=make_medical_Record('David',1)




class Tree():
    def __init__(self, entry, left=None, right=None):
        self.entry = entry
        self.left = left
        self.right = right
    def __repr__(self):
        if not self.left and not self.right:
            return "Tree({0})".format(repr(self.entry))

        return "Tree({0},{1},{2})".format(repr(self.entry),repr(self.left),repr(self.right))


def build_tree(tree):
    if len(tree) == 1:
        return Tree(tree,None,None)
    return Tree(tree[0],build_tree(tree[1]),build_tree(tree[2]))

def max_tree(tree):
    """Get the max element in a tree"""
    if not tree:
        return None
    maximum = tree.entry
    if tree.left != None:
        maximum = max(maximum, max_tree(tree.left))
    if tree.right != None:
        maximum = max(maximum, max_tree(tree.right))

    if type(maximum) is tuple: maximum = maximum[0]
    return maximum

tree1 = (12, (6, (2,), (8,)), (15, (14,), (18,)))
t1=build_tree(tree1)