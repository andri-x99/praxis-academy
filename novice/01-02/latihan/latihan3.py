#!/bin/usr/python

tel = {'jack': 4098, 'sape':4139}
tel['guido'] = 4127
print(tel)

tel['irv'] = 4199
print(list(tel))
print(sorted(tel))
dict([('sape',4139),('jack',4098),('guido',1999)])

