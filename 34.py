tinytuple = (123, 'john')

print(2 * tinytuple)

try:
	tinytuple.append("Reva")
	print(tinytuple)
except:
 	print("Immutable data starcture")


"""
KeyError is thrown when a key is not found.
>>> D1={'1':"aa", '2':"bb", '3':"cc"}
>>> D1['4']
Traceback (most recent call last):
File "<pyshell#15>", line 1, in <module>
D1['4']
KeyError: '4'


IndexError is thrown when trying to access an item at an invalid index.
>>> L1=[1,2,3]
>>> L1[3]
Traceback (most recent call last):
File "<pyshell#18>", line 1, in <module>
L1[3]
IndexError: list index out of range



NameError is thrown when an object could not be found.
>>> age
Traceback (most recent call last):
File "<pyshell#6>", line 1, in <module>
age
NameError: name 'age' is not defined


AttributeError - Raised on the attribute assignment or reference fails.
"""
