number = input("¿Qué número deseas saber si es par o impar? >")
enable = True

while enable:

    try:
        if int(number) % 2 == 0:
            print(f'El número {number} es par')
            enable = False
        else:
            print(f'El número {number} es impar')
            enable = False
    except:
        number = input("Que escribas un número ")