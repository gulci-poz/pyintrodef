# stringi są immutable, nie da się zmienić lub wstawić znaku w miejscu o danym indeksie
# sekwencje znaków
poem = """wiersz 1
wiersz 2"""
print(poem)
print(str(99.9))
# print() korzysta ze str() do drukowania obiektów nie będących stringami i interpolacji
print('\'\t\"\t\\\nescapes')
print('spacja' ' ' 'konkatenacja')
print('plus' + ' ' + 'konkatenacja')
print('print', 'konkatenacja')
print('hello ' * 3)
print('hello'[0])
print('hello'[-1])
print('hello'.replace('h', 'H'))
print('Y' + 'hello'[1:])

alphabet = 'abcdefghijklmnopqrstuvwxyz'
# [start, end)
# w prawo
print(alphabet[-3:])
# w lewo, bo określamy krok -1
print(alphabet[-3::-1])
# w prawo
print(alphabet[-3:-1])
# w lewo, ale musimy określić krok, inaczej dostaniemy pusty string
print(alphabet[-1:-3:-1])
print(alphabet[:])
print(alphabet[::-1])
# można przekroczyć zakres
# jeśli jest poza dolnym, to dostaniemy 0
# jeśli jest poza górnym, to dostaniemy -1
print(alphabet[-50:50])
# jeśli jesteśmy poza zakresem, to dostaniemy pusty string
print(alphabet[50:51])
print(alphabet[-50:-51])
print(len(alphabet))

numeros = "uno, dos, tres, quatro"
print(numeros.split(','))
# brak separatora - nowa linia, spacja lub tab
print(numeros.split())

numeros = "uno,dos,tres,quatro"
print(numeros)
splitted = numeros.split(',')
print(' '.join(splitted))
print(numeros.startswith('uno'))
print(numeros.endswith('dos'))
# pierwsze wystąpienie
print(numeros.find(','))
print(numeros.rfind(','))
print(numeros.count(','))
print(numeros.isalnum())
print(numeros.isalpha())
numeros = '.' + numeros + '.'
print(numeros)
print(numeros.strip('.'))
print(numeros.lstrip('.'))
print(numeros.rstrip('.'))
name = 'gulci'
print(name.capitalize())
print(name.capitalize().swapcase())
print(name.lower())
print(name.upper())
print(name.center(30))
print(name.ljust(30))
print(name.rjust(30))
# możemy określić, ile instancji zastąpić
print('aaaaaaaaaa'.replace('a', 'h', 5))
