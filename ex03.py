# listy

days = ['Pn', 'Wt', 'Sr', 'Czw', 'Pt', 'Sob', 'Nd']
months = list()

print(days)
print(months)

# konwersja stringa na listę znaków
name = list('sebastian')
print(name)

# konwersja tuple do listy
tup = ('uno', 'dos', 'tres')
tupl = list(tup)
print(tupl)

# zapisanie wartości do listy za pomocą split()
date = '24/05/2016'
datel = date.split('/')
print(datel)
print(datel[2])
print(datel[-1])

llist = [['a', 'b', 'c'], [1, 2, 3], ['do', 're', 'mi']]
print(llist[2][1])
print(llist[2][::-1])
# dodajemy listę jako jeden element, a nie poszczególne jej elementy
llist.append(['uno', 'dos', 'tres'])
others = ['jeden', 'dwa', 'trzy']
others_more = ['cztery', 'piec', 'szesc']
# extend() dodaje pojedyncze elementy, a nie listę jako całość
llist.extend(others)
llist += others_more
print(llist)
# insert dodaje przed określoną wartością
# z 0 dodaje na początku
# z wartością poza zakresem dodaje na końcu
llist.insert(2, 'hello')
llist.insert(15, 'hello')
print(llist)
# odłączenie nazwy od obiektu i jeśli była to ostatnia referencja, zwolnienie pamięci
del llist[-1]
del llist[0]
print(llist)
llist.append('hello')
# usuwa pierwsze wystąpienie elementu
llist.remove('hello')
print(llist)
# pop() zwraca ściągany z listy element, domyślnie -1, można podać argument
llist = ['a', 'b', 'c', 'd']
print(llist)
print(llist.pop())
print(llist.pop(1))
print(llist)
llist.append('a')
print(llist)
# indeks pierwszego wystąpienia
print(llist.index('a'))
# pythonic way
print('c' in llist)
print('b' in llist)
print(llist.count('a'))
# join() działa na stringu, argumentem jest iterowalna sekwencja stringów, nie tylko lista
# działanie odwrotne do split()
lstring = ','.join(llist)
print(lstring)
slist = ['g', 'b', 'a', 'z', 'k']

# sortowanie
# można mieszać np. int i float
# reverse=True
# zwraca kopię listy
print(sorted(slist))
# sortowanie in place, z zapisem do zmiennej
slist.sort()
print(slist)
slist.sort(reverse=True)
print(slist)
print(len(slist))

# tworzymy referencję, każda zmiana będzie odzwierciedlona w obu listach
slist2 = slist
slist2[2] = 10
print(slist)
print(slist2)

# tworzenie kopii listy
copy1 = slist.copy()
copy2 = list(slist)
copy3 = slist[:]
copy1[2] = 11
copy2[2] = 12
copy3[2] = 13
print(copy1)
print(copy2)
print(copy3)
