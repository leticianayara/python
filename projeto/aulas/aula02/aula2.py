# \r\n - CRLF (Windows)
# \n - LF(MA=ac)
print(12, 34, 1011, sep='-', end='\r\n')
print(56, 78, sep="-", end='\n')
print(9, 10, sep="-", end='\n')
print()
print(12, 34, 1011, sep='-', end='##')
print(56, 78, sep="-", end='\n')
print()
print(12, 34, 1011, sep='-', end='##\n')
print(56, 78, sep="-", end='\n')
print()
print(12, 34, 1011, sep='-', end='\n##')
print(56, 78, sep="-", end='\n')