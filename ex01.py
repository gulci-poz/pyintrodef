a = 10
b = 3.14
c = True
d = "hello"

print(type(a))
print(type(b))
print(type(c))
print(type(d))

print(10 // 3)
print(10 / 3)
print(10 ** 3)
print(-59)
print(a - 4)
a += 21
print(a)
a /= 3
print(a)
print(15 % 4)
# divmod() zwraca tuple
print(divmod(15, 4))
print(divmod(9, 5))

# można używać małyhc lub wielkich b, o, h
print(0b10)
print(0o10)
print(0x10)

print('konwersja do int')
print(int(True))
print(int(False))
print(int(99.9))
print(int(1.0e4))
print(int('55'))
print(int('+45'))
print(int('-6'))
# nie uda się konwersja stringa z liczbą typu float lub w postaci wykładnikowej
print(4 + 7.0)
print(True + 2)
print(False + 3.0)
# jest jeszcze funkcja float o podobnym działaniu

googol = 10 ** 100
print(googol)
print(googol * googol)
