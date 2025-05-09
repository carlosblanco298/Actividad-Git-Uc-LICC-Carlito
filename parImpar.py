number = input("¿Qué número deseas saber si es par o impar?")

while number == "":
    number = input("Que escribas un número")

if int(number) % 2 == 0:
    print(f'El número {number} es par')
else:
    print(f'El número {number} es impar')
