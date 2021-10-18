'''A string is a sequence of characters. A character in the string can be accessed through the
index operator using the syntax:
s[index]
The indexes are 0 based; that is, they range from 0 to len(s)-1'''
s = 'Welcome'
print(s[-1]) # e
print(s[-2]) # m

'''In line 2, s[-1] is the same as s[-1 + len(s)] , which is the last character in the string. In
line 4, s[-2] is the same as s[-2 + len(s)] , which is the second last character in the string.
Note that since strings are immutable, you cannot change their contents. For example, the
following code is illegal:
s[2] = 'A'''