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