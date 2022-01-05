#dipatch technique
def shmeasy_park(fee):
    time, money = 0, 0
    def charge(amount):
        nonlocal money
        money += amount
    def park(t):
        nonlocal time,money
        cost = t*fee
        if cost > money:
            return 'No money'
        money -= cost
    def dispatch(m,v):
        if m == 'charge':
            return charge(v)
        elif m == 'park':
            return park(v)
        else:
            return 'Unknown message {}'.format(m)
    return dispatch

#dispatch dictionary technique
def shmeasy_park_dict(fee):
    time,money = 0,0
    def charge(amount):
        nonlocal money
        money += amount
    def park(t):
        nonlocal time, money
        cost = t * fee
        if cost > money:
            return 'No money'
        money -= cost
        return 'Balance left: {}'.format(money)
    return {'charge':charge, 'park': park}

class Time(object):
    def __init__(self,h,m,s):
        if 0 > s >= 60: s = 0
        if 0 > m >= 60: m = 0
        if 0 > h >= 24: h = 0
        self.h,self.m,self.s = h,m,s
    def printTime(self):
        print("{:02d}:{:02d}:{:02d}".format(self.h,self.m,self.s))
    def TimeToInt(self):
        return self.h * 3600 + self.m * 60 + self.s
    def IntToTime(self,time):
        self.h = time // 3600
        self.m = time // 60 % 60
        self.s = time % 60
        return self
    def Later(self,time):
        if time.h > self.h: return True
        if time.m > self.m: return True
        if time.s > self.s: return True
        return False
    def addSecond(self):
        self.s += 1
        if self.s == 60: self.s, self.m = 0, self.m + 1
        if self.m == 60: self.m, self.h = 0, self.h + 1
        if self.h == 24: self.h = 0

    def __add__(self,time):
        s = time.TimeToInt()
        for i in range(s):
            self.addSecond()
        return self

    def __sub__(self, s):
        for i in range(s*3600*24-s):
            self.addSecond()
        return self
    def __str__(self):
        return "{:02d}:{:02d}:{:02d}".format(self.h,self.m,self.s)

a = Time(1,10,15)

a.printTime()
print(a.TimeToInt())
Time.IntToTime(a,4216).printTime()
a.printTime()

b = Time(23,59,59)
b.printTime()
b.addSecond()
b.printTime()

print("ADD")
c = Time(9,45,00)
d = Time(1,35,00)
c += d
c.printTime()

print("SUB")
f = Time(1,10,16)
(f-5).printTime()

print(f.__str__())



