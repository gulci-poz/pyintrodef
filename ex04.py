# tuple - immutable, constant list

# nie musimy używać nawiasów przy definicji krotki
# jedynie przy pustej są konieczne
# elementem definiującym jest przecinek
empty_tuple = ()
one_el_tuple = 'fname',
more_el_tuple = 'fname', 'lname'
print(empty_tuple)
print(one_el_tuple)
print(more_el_tuple)

# tuple unpacking - możliwość zadeklarowania kilku zmiennych z wartościami z tuple
a, b = more_el_tuple
print(a)
print(b)

spring = 'spring'
summer = 'summer'
spring, summer = summer, spring
print('spring:', spring)
print('summer:', summer)

# konwersja
alist = ['spring', 'summer', 'autumn', 'winter']
atuple = tuple(alist)
print(atuple)

# krotki zajmują mniej pamięci niż listy
# krotki można używać jako zbioru kluczy do słownika
# named tupled - alternatywa do obiektów
# argumenty do funkcji są przekazywane jako krotki
