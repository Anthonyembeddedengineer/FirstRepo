# Crea una calculadora con multiple operandos. 

# Para crear esta calculadora usamos la función eval().


# Set de datos 

history = []

print('start')
import math 

# Define allowed names (functions/constants)

def sin_deg(x):
    return math.sin(math.radians(x))

def cos_deg(x):
    return math.cos(math.radians(x))

def tan_deg(x):
    return math.tan(math.radians(x))

# Agregale funciones trigonometrica al codigo. 

allowed_names = {
    'sin' : sin_deg,
    'cos' : cos_deg,
    'tan' : tan_deg,
    'pi'  : math.pi,
    'e'   : math.e,
    'sqrt': math.sqrt,
    'log' : math.log,
    'log10': math.log10
}

# Example: eval with math functions

def calculadora():
        
    while True:
        expression = input('Enter an operation or "q" to quit: ')
        
        if expression.lower() == 'q': 
            break

        try:
            result= eval(expression, {"__builtins__": {}}, allowed_names)
            print('Result: ', round(result, 1))
            history.append(result)
        
        except Exception as e: 
            print('Not valid,', e)

# Historial de la calculadora

def calculator_history():
    if not history:
        print('No history available.')
    else:
        print('History:')
        for i, result in enumerate(history, start=1):
            print(f'{i}: result = {round(result, 1)}')
    turn_back = input('Do you want to return to the calculator (y/n)?: ')
    if turn_back.lower() == 'y':
        return calculadora()
    else:
        print('Exiting calculator. Goodbye!')

calculadora()
calculator_history()


## Una vez terminado de ver el historial haz que devuelva la función calculadora() con una pregunta

