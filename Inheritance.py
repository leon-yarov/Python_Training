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
            if name in attrs: return attrs[name]
            else:
                value = cls['get'](name)
                print(value, name, "base")
                if callable(value): return lambda *args: value(obj,*args)
                else: return value
        def set(name, value):
            attrs[name] = value

        obj = {'get': get, 'set': set}
        init = get('__init__')
        if init: init(*args)
        return obj
    cls = {'get': get, 'set': set, 'new': new}
    return cls

def make_point_class():
    color = 'blue'
    def __init__(self,x,y):
        self['set']('x',x)
        self['set']('y',y)

    def str(self):
        return '(x=%d, y=%d)' % (self['get']('x'), self['get']('y'))

    def prt(self):
        print(self['get']('str')())

    def shift(self,number):
        self['set']('x', self['get']('x') + number)
        self['set']('y', self['get']('y') + number)

    def eq(self,other):
        return self['get']('x') == other['get']('x') and self['get']('y') == other['get']('y')

    return make_class(locals())

Point = make_point_class()

def make_colorpoint():
    color = 'red'
    def str(self):
        # print(self['get']('str'))
        print(self['get']('shift'))
        return self['get']('str') + ' [color =%s]' % self['get']('color')

    return make_class(locals(),Point)


ColorPoint = make_colorpoint()


p = Point['new'](1,2)
q = ColorPoint['new'](3,4)
q2 = ColorPoint['new'](5,6)
p['get']('prt')()
print(q['get']('str')())
# q['get']('prt')()
# p['get']('shift')(3)
# p['get']('prt')()
# print(q['get']('eq')(q))
# q.color = 'green'
# q.prt()
# q2.prt()
# TODO: fix the ColorPoint 'get' not working





