'''
The slicing operator returns a slice of the string using the syntax s[start : end] . The slice
is a substring from index start to index end – 1 .
'''

s = "Welcome"
print(s[1 : 4]) # elc
'''
s[1 : 4] returns a substring from index 1 to index 3 .
'''

'''
The starting index or ending index may be omitted. In this case, by default the starting
index is 0 and the ending index is the last index. For example,
'''

s = "Welcome"
print(s[ : 6]) # Welcom
print(s[4 : ]) # ome
print(s[1 : -1]) # elcom