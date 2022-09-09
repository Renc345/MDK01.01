1
a = int(input())
while a != -1:
    print('Осталось секунд:',a)
    a -= 1
print('Пуск')

a = int(input())
for a in range(a,-1,-1):
    print('Осталось секунд:',a)
print('Пуск')

2
n = int(input())
space = n-1
star = 1
for i in range(1, n + 1):
    print(' '*space + '*'*star)
    space -= 1
    star += 2

3
a = int(input())
iq = int(input())
print(0)
for i in range(1, a + 1):
    b = int(input())
    if b > iq:
        print('>')
    elif b < iq:
        print('<')
    else:
        print(0)
    iq = (iq * i + b) / (i + 1)

5
password = input()
password2 = input()
while len(password) < 8:
    print("Короткий!")
    password = input()
    password2 = input()
while "123" in password:
    print("Простой!")
    password = input()
    password2 = input()
while password2 != password:
    print("Различаются.")
    password = input()
    password2 = input()
else:
    print("OK")

7
price = float(input())
total = 0
while price >= 0:
    if price >= 1000:
        price = price - price * 0.05
    total = total + price
    price = float(input())
print(total)


