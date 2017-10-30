title = input('Enter a title for the data: ')
print('You entered:', title)
header1 = input('Enter the column 1 header: ')
print('You entered:', header1)
header2 = input('Enter the column 2 header: ')
print('You entered:', header2)
data = input('Enter a data point (-1 to stop input):')
data_list = data.split(',')
i = str(data_list[len(data_list) - 1])
i = i.replace(' ', '')
string = data_list[0]
integer = i
string_list = []
integer_list = []
while data != '-1':
    if ',' not in data:
        print('Error: No comma in string.\n')
        data = input('Enter a data point (-1 to stop input):')
        continue
    elif data.count(',') > 1:
        print('Error: Too many commas in input\n')
        data = input('Enter a data point (-1 to stop input):')
        continue
    elif not integer.isdigit():
        print('Error: Comma not followed by an integer\n')
        data = input('Enter a data point (-1 to stop input):')
        data_list = data.split(',')
        i = str(data_list[len(data_list) - 1])
        i = i.replace(' ', '')
        string = data_list[0]
        integer = i
        continue
    print('Data string:', string)
    print('Data integer:', integer)
    string_list.append(string)
    integer_list.append(integer)
    data = input('Enter a data point (-1 to stop input):')
    data_list = data.split(',')
    i = str(data_list[len(data_list) - 1])
    i = i.replace(' ', '')
    string = data_list[0]
    integer = i
print('\n %33s \n' % title)
print('\n %-20s %-10s %-23s \n' % (header1, '|', header2))
print('--------------------------------------------')
for i in range(0, len(string_list)):
    print('\n %-20s %-10s %-23s' % (string_list[i], '|', integer_list[i]))
for i in range(len(integer_list)):
    integer_list[i] = int(integer_list[i])
for i in range(0, len(string_list)):
    print('\n %20s %-5s' %(string_list[i], ' '), end = '')
    for j in range(0, integer_list[i]):
        print('*', end='')
          
                
    

