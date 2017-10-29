name = str(input('Enter first, middle, and last name:\n'))
separator = ' '
names = name.split(separator)
sep = ". "
I = (names[0][0],names[1][0],(names[2][0]))
initals = sep.join(I)
print(initals + '.')


