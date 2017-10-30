def initials():
    first = input('Enter your first name: ')
    middle = input('Enter your middle name: ')
    last = input('Enter your last name: ')
    print('Initials: %s.%s.%s' % (first[0], middle[0], last[0]))
def num_translator():
    number = input('Enter a ten character phone number(XXX-XXX-XXXX): ')
    number = number.replace('A', '2')
    number = number.replace('B', '2')
    number = number.replace('C', '2')
    number = number.replace('D', '3')
    number = number.replace('E', '3')
    number = number.replace('F', '3')
    number = number.replace('G', '4')
    number = number.replace('H', '4')
    number = number.replace('I', '4')
    number = number.replace('J', '5')
    number = number.replace('K', '5')
    number = number.replace('L', '5')
    number = number.replace('M', '6')
    number = number.replace('N', '6')
    number = number.replace('O', '6')
    number = number.replace('P', '7')
    number = number.replace('Q', '7')
    number = number.replace('R', '7')
    number = number.replace('S', '7')
    number = number.replace('T', '8')
    number = number.replace('U', '8')
    number = number.replace('V', '8')
    number = number.replace('W', '9')
    number = number.replace('X', '9')
    number = number.replace('Y', '9')
    number = number.replace('Z', '9')
    print('Numeric Number:', number)
def counter():
    string = input('Enter a string: ').lower()
    vowels = 0
    consonants = 0
    new_list = list(string)
    for i in new_list:
        if i in 'aeiou':
            vowels += 1
        if i in 'bcdfghjklmnpqrstvwxyz':
            consonants += 1
    print('Number of Vowels:', vowels)
    print('Number of Consonants:', consonants)
def pig_latin():
    sentence = input('Enter a sentence: ')
    sentence = sentence.replace('.', '')
    sentence = sentence.split()
    new_sentence = []
    final_sentence = ''
    for i in sentence:
        i = i + i[0]
        i = i[1:]
        i = i.upper()
        i = i + 'AY'
        new_sentence.append(i)
    for i in new_sentence:
        final_sentence = final_sentence + i + ' '
    final_sentence = final_sentence[:-1]
    final_sentence += '.'
    print(final_sentence)
pig_latin()

    


          
