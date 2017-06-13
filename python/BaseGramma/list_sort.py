# sorted would not change a
a = [2, 3, 5, 1, 9]
sorted(a)
sorted(a, reverse=True)

f = [{'name':'abc','age':20},{'name':'def','age':30},{'name':'ghi','age':25}]

# by lambda
sorted(f, key=lambda k : k['age'])

# by function
def age(f):
    return f['age']
sorted(f, key=age)

# in class
class Foo(object):
    def __init__(self, score):
        self.score = score
    def __lt__(self, other):
        return self.score < other.score

l = [Foo(3), Foo(1), Foo(2)]
# change l
l.sort()
# not change l
sorted(l)
