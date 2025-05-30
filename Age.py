# Crea un codigo que te diga si un niño es mayor o menor de edad.
'''
def age():
    age = int(input('Ingresa tu edad: '))
    if age >= 18 and age < 90:
        print('You are of legal age')
    elif age >= 90:
        print('You are probably dead by now')
    elif age < 0:
        print('You are not even born yet jajaja')
    else:
        print('You are NOT of legal age')
age() '''


# Crea un codigo que te permita categorizar la altura de un hombre adulto.

def height():
    height = float(input('Ingresa tu altura: '))
    if height >= 1.50 and height <= 1.59:
        print('You are a fucking oompa loompa')
        print(f'Your height is {height} mts')
    elif height >= 1.60 and height <= 1.69:
        print('You are short height')
        print(f'Your height is {height }mts')
    elif height >= 1.70 and height <= 1.79:
        print('You are average height!')
        print(f'Your height is {height} mts')
    elif height >= 1.80 and height <= 1.89:
        print('You are a tall')
        print(f'Your height is {height} mts')                
    elif height >= 1.90 and height <= 1.99:
        print('You are taller than tallers')
        print(f'Your height is {height} mts')
    elif height >= 2.0 and height <= 2.30:
        print('You are a fucking giant!')
        print(f'Your height is {height} mts')
    else:
        print('Ingresa un numero valido')

height()