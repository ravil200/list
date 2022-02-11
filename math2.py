'''
#0
a = {3,10,11,13,31,21,1,10,3,5,6,6}
a.remove(6)
print(a)
#1
a = {"dog", "cat", "mouse", "sheep"}
b = {"cow", "horse", "donkey", "cat", "dog"}
b.intersection_update(a, b)
print(b)
#2
a = {"cow", "horse", "donkey", "cat", "dog"}
b = {"dog", "cat", "mouse", "sheep"}
c = a.difference(b)
print(c)
#3
a = {345,9,"cat", "house", "sheep"}
a.pop()
print(a)
#000
a = {'lagman': 120, 'plov': '120', 'borsh': 100}
a.update({'besh_barmak': 130})
a.update({'lagman': 135})
a.pop('borsh')
print(a)
#10
menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
menu.update({'drinks': ['Cola-Cola', 'Fanta', 'Sprite']})
print(menu)
#020
s = {"add", "update", "remove", "clear", "difference", "discard", "pop", "intersection", "intersection_update"}
d = {"clear", "get", "keys", "values", "items", "update", "tuple", "set", "dict", "list"}
a = s.intersection(d)
print(a)
#31
#while True:
	l = {}
	a = input('name:')
	b = input('password:')
	c = input('name:')
	d = input('password:')
	if a == c and b==d:
		t = input('nam:')
		p = input('pass:')
		if t == c and p == d:
			l[a,c,t]=b,d,p
			print(l)
		else:
			print('последняя не правильно')
	else:
		print('не провильно')

#27
a = {input('введите имя') : input('job'), input('введите имя') : input('job'), input('введите имя') : input('job'), input('введите имя') : input('job'), input('введите имя') : input('job')}
s = a.keys()
v = a.values()
print('Hello guy {}, best job {}'.format(s,v))
#22
a = {input('введите число'), input('введите число'), input('введите число'), input('введите число'), input('введте число'), input('введте число'), input('введте число'), input('введте число'), input('введте число'), input('введте число')}
print(a)
#24
a = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Ecuador', 'Guyana', 'Paraguay', 'Peru', 'Suriname', 'Suriname', 'Uruguay', 'Venezuela']
print(a.intersection_update())
'''
a = {''}
b = {input('item'), input('item'), input('item'), input('item'), input('item')}
a.add(b)
a.pop()
print(a)
