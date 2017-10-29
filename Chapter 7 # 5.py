tele = input('Enter 10-character Alphabetic Telephone Number:\n')
    #example 555-GET-FOOD
    #A,B,C = 2  D,E,F = 3  G,H,I = 4 J,K,L =5
    #M,N,O = 6  P,Q,R,S = 7  T,U,V = 8 W,X,Y,Z = 9

#Copy the original input
Fixed = tele[:]


#Google Translations
Fixed = Fixed.replace('A', '2')
Fixed = Fixed.replace('B', '2')
Fixed = Fixed.replace('C', '2')
Fixed = Fixed.replace('D', '3')
Fixed = Fixed.replace('E', '3')
Fixed = Fixed.replace('F', '3')
Fixed = Fixed.replace('G', '4')
Fixed = Fixed.replace('H', '4')
Fixed = Fixed.replace('I', '4')
Fixed = Fixed.replace('J', '5')
Fixed = Fixed.replace('K', '5')
Fixed = Fixed.replace('L', '5')
Fixed = Fixed.replace('M', '6')
Fixed = Fixed.replace('N', '6')
Fixed = Fixed.replace('O', '6')
Fixed = Fixed.replace('P', '7')
Fixed = Fixed.replace('Q', '7')
Fixed = Fixed.replace('R', '7')
Fixed = Fixed.replace('S', '7')
Fixed = Fixed.replace('T', '8')
Fixed = Fixed.replace('U', '8')
Fixed = Fixed.replace('V', '8')
Fixed = Fixed.replace('W', '9')
Fixed = Fixed.replace('X', '9')
Fixed = Fixed.replace('Y', '9')
Fixed = Fixed.replace('Z', '9')


#Print the translated string
print(Fixed)

