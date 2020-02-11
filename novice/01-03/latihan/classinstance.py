class Dog:
    kind='canine'

    def __init__(self,name):
        self.name = name

d=Dog('Johny')
# print(d)
e=Dog('Zranc')
# print(e)
f=Dog('Diza')
# print(f)
print(d.kind)
print(d.name)
print(e.name)
print(f.name)