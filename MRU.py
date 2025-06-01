# Crear un codigo que te resuelva cualquier ejercicio de M.R.U a través de los datos del problema
# Autores: Anthony Viveros

# Set de datos

history = []

# Formulas para obtener distancias, velocidad y tiempo en MRU 

def distancia():

    x = int(input('Ingresa la velocidad(en m/s): '))
    y = int(input('Ingresa el tiempo(en segundos): '))
    result = x * y 
    result_print = f'La distancia recorrida es de: {result}mts'
    print(result_print)
    history.append(result_print)

def velocidad():

    x = int(input('Ingresa la distancia(en mts): '))
    y = int(input('Ingresa el tiempo(en segundos): '))
    result = x / y
    result_print = f'La velocidad del objeto es de: {result}m/s'
    print(result_print)
    history.append(result_print)

def tiempo():

    x = int(input('Ingresa la distancia(en mts): '))
    y = int(input('Ingresa la velocidad(en m/s): '))
    result = x / y
    result_print = f'El tiempo que se demoro en recorrer {x} mts es de: {result}s'
    print(result_print)
    history.append(result_print)

def MRU_calculator():
    while True:
        
        option = input('Choose an option to calculate the variable (1,2,3,4) "q" to quit: ')

        if option == 'q':
            print('Exiting the calculator...')
            break

        try:

            if option == '1':
                print('------------ The distance will be calculated ----------\n')
                distancia()

            elif option == '2':
                print('------------ The velocity will be calculated -----------\n')
                velocidad()

            elif option == '3':
                print('------------ The time will be calculated --------------------\n')
                tiempo()
            
            elif option == '4':
                print('History: \n')
                MRU_history()


        except ValueError:
                print('Opps! Enter only number not words')
        


def MRU_history():
    if not history:
        print('No history available')
    else:
        print('------History------')
        print()
        for i, result in enumerate(history, start=1):
            print(f'{i} result: {result}' )
    turn_back = input('Do you want to use the MRU calculator again? yes = Y: ')
    if turn_back.lower() == 'Y':
        MRU_calculator()
    else:
        ('Exiting the calculator...')

MRU_calculator()


        

