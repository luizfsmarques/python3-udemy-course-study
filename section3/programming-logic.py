# Code comment
print(123) # comment

"""
Docstrings
with double quotes
The interpreter read, but it does not run; keep only in memory.
"""

'''
Docstrings
with single quotes
The interpreter read, but it does not run; keep only in memory.
'''

# Print function
# It is used to show something on the screen/terminal.
# Unnamed and named arguments
print(25,45, sep="-",end="##\r\n")
print(35,45,sep='-',end='\n')
print('Hello world')

# Obs.: Python is dinamically and strongly typed.

# Data type: string
# It is used to represent text.
print('Luiz')
print("Luiz")
print("Luiz \"Fernando\"")
print(r"Luiz \"Fernando\"")
print("Luiz 'Fernando'")
print('Luiz "Fernando"')

# Data type: int
# It is used to represent integers.
print(1)
print(-1)
print(0)

# Data type: float
# It is used to represent decimal numbers (Floating point).
print(1.0)
print(-1.0)
print(0.0)

# Type class
# It is used to show, the data type.
print(type(1))
print(type('Luiz'))
print(type(2.0),type(-2.0),type(0.0))

# Data type: bool
# It represents the value True or False.
print(True)
print(False)
print(10==10)
print(10==11)
print(type(True), type(False), type(10==10))

# Variables
# It is used to represent memory spaces and its values.
full_name = 'Luiz Marques'
age = 30
of_legal_age = age >= 18
print('Name: ',full_name,'Age: ',age)
print('of_legal_age?',of_legal_age)

# Arithmetic operators
# It is used to execute some operation
addition = 10 + 10
subtraction = 10 -5
multiplication = 10 * 10 
floor_division = 10 // 3
exponentiation = 2 ** 10
modulus = 10 % 2


# Other uses to operators + and *
concatenation = 'Luiz' + str(1) + ' ' + 'Marques'
print(concatenation)

repeting_a = 'A' * 10
repeting_luiz = 3 * 'Luiz'
print(repeting_a)
print(repeting_luiz)

# Operator precedence ( order of operations)
# 1. (n + n)
# 2. **
# 3. * / // %
# 4. + -
count_1 = 1 + 1 ** 5 + 5 # 7
count_2 = (1 + int(0.5 + 0.5)) ** (5 + 5) # 1024
print(count_1,count_2,sep=' ---- ')

# Ellipsis
# It can be used to indicate that will be replaced by a content.
imc = ...

#f-strings
#It can be used to format the strings in easy way.
name = 'Luiz'
height = 1.69
weight = 100
bmi = weight/height**2

line_1 = f'{name} have {height:.2f} meters of height,'
line_2 = f'his {weight} is kg and his bmi (body mass index) is'
line_3 = f'{bmi:.2f}'

print(line_1)
print(line_2)
print(line_3)

#Format method from the string object
#It is used to format strings.
a = 'A'
b = 'B'
c = 1.1

string = 'a={} b={} c={:.2f}'
formating = string.format(a,b,c)
print(formating)

string = 'a={0} c={2:.4f} b={1}' # Using arguments indexes
formating = string.format(a,b,c)
print(formating)

string = 'a={name1} c={name3:.5f} b={name2}'
formating = string.format(name1=a,name2=b,name3=c)
print(formating)

