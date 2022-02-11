'''
#0
a = [(5, 'hello', ), 999,'ok',(987654, 'good'), 576,'6537.87',(34567.7,'615')]
print(a)

#1
a = tuple(['Ravil' ,1234, '3542.9' ,'hello', 764])
print(a[0:], len(a))
#22
a = list('Ravil' ,123, 'true' ,123456.9876, 
#3
a = ['Jack', 'Jimmy', 'Jackson', 'Jhon', 'Jackson']
b = ' '
print(b.join(a))
#4
a = ['Jack', 'Jimmy',1234.56789, 'Jhon', 'Jackson']
b = ['Ravil',123456789,'Madiar']
print(a+b)
#5
a = ['Jack', 'Jimmy', 'Jackson', 'Jhon', 'Jackson', 'Jhon',  'Jimmy', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon',]
print(a.count('Jack'))
#6
a = ['Jack', 'Jimmy', 'Jackson', 'Jhon', 'Jackson', 'Jhon',  'Jimmy', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon',]
print(a.remove('Oskar'))
#7
a = ['Ravil',2006,'PYTHON']
print(a)
#8
a = ["int", "str", "bool", "if", "else", "elif", "loop", "tuple", "list", "None", True, False]
print(a.index("loop"))
print(a.pop(6))
#9
a = [123, 321, 2, 543, 64, 463, 234, 867, 6234, 63246, 3, 43]
b = a[0]*a[1]*a[2]*a[3]*a[4]*a[5]*a[6]*a[7]*a[8]*a[9]*a[10]*a[11]
print(b)
#10
list1 = ['aszdfxgch','75','5867','8768','ghfj']
letters = []
numbers = []

if list1[0].isalpha():
	letters.append(list1[0])
elif list1[0].isdigit():
	numbers.append(list1[0])
if list1[1].isalpha():
	letters.append(list1[1])
elif list1[1].isdigit():
	numbers.append(list1[1])
if list1[2].isalpha():
	letters.append(list1[2])
elif list1[2].isdigit():
	numbers.append(list1[2])
if list1[3].isalpha():
	letters.append(list1[3])
elif list1[3].isdigit():
	numbers.append(list1[3])
if list1[4].isalpha():
	letters.append(list1[4])
elif list1[4].isdigit():
	numbers.append(list1[4])
print(letters)
print(numbers)
#11
a = ["int", "str", "bool", "if", "else", "elif", "loop", "tuple", "list", "None", True, False]
print(a[0:3])
'''
