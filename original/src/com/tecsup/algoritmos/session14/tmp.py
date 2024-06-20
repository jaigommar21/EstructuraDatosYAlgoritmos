import math

print(dir(math))

print(__name__)

var = 10
assert var !=0

try:
    raise Exception
except BaseException:
    print("a")
except Exception:
    print("b") 
except:
    print("c")   

x = "\\\\"
print(len(x))


print(chr(ord("p")+2))

print(float("1.3"))

class A:

    def __init__(self, v = 2):
        self.v = v
    
    def set(self, v = 1):
        self.v += v
        return self.v

a = A()
#b = a
#b.set()
a.set()
print(a.v)



class MiClass:
    def __init__(self, v):
        self.a = v + 1

mc = MiClass(0)
print(mc.a)


class A:

    def a(self):
        print("a")

    def x(self):
        print("yyyyyy")

class B:

    def a(self):
        print("b")

    def x(self):
        print("xxxxx")

class C(B,A):

    def c(self):
        self.a()
        self.x()

c = C()
c.c()


def I(n):
    s = "+"
    for i in range(n):
        s += s
        #print(">>>>",s)
        yield s
        #print("---",s)

# print(I(2))
for x in I(2):
    print(x,end="")

