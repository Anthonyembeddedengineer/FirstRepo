
import random

# Codigo donde se pone a prueba las operaciones booleanas para practicar

# Juego de afirmaciones 

# Datos de repuestas acertadas

count = 0

afirmaciones = {
    'Sin fuego no hay humanidad tal como la conocemos' : True,
    'En 1776 las 13 colonias britanica declararon su independencia conformando lo que es hoy USA' : True,
    'Cristobal Colon llego al continente americano en 1493' : False,
    'El imperio romano fue uno de los mas influyentes en la historia': True,
    'La caida del muro de berlin no reunifico alemania': False,
    'La Revolución Francesa comenzó en 1789': True,
    'Napoleón Bonaparte fue emperador de Francia antes de la Revolución Francesa': False,
    'La Primera Guerra Mundial terminó en 1918': True,
    'La escritura fue inventada después de la imprenta': False,
    'La Declaración Universal de los Derechos Humanos fue proclamada en 1948': True,
    'Los mayas desaparecieron completamente antes de la llegada de los españoles': False,
    'La peste negra mató a aproximadamente un tercio de la población europea en el siglo XIV': True,
    'Albert Einstein desarrolló la teoría de la evolución': False,
    'La civilización egipcia se desarrolló a orillas del río Nilo': True,
    'La Segunda Guerra Mundial comenzó en 1945': False
}
# Recorremos las afirmaciones

afirmaciones_random = list(afirmaciones.items()) 
random.shuffle(afirmaciones_random) # Sorteamos las preguntas aleatoriamente con shuffle

for preguntas, respuesta_correcta in afirmaciones_random:
    print('\nVerdadero o falso?: ', preguntas)

    # Le preguntamos al usuario por su respuesta
    respuesta_usuario = input('\nIngresa "verdadero" o "falso": ').lower().strip()

    # Transformamos las respuestas a booleanos
    if respuesta_usuario == 'verdadero':
        respuesta_usuario_bool = True
        
    elif respuesta_usuario == 'falso': 
        respuesta_usuario_bool = False
        
    else:
        print('Entrada incorrecta. Ingresa "verdadero" o "falso"')
        continue # Continua la siguiente pregunta

    # Hacemos un codigo que evalue la respuesta del usuario y que coincida con la respuesta real

    if respuesta_usuario_bool == respuesta_correcta:
        print('Correcta!')
        count += 1
    else:
        respuesta_texto = 'verdadero' if respuesta_correcta else 'false'
        print(f'La respuesta correcta es {respuesta_texto}!') 

# Contador de respuestas acertadas

print(f'\nRespuesta acertadas: {count}')

# Medidor de conocimiento general

if count <= 5 and count >= 0:
    print('Mejora tu conocimiento general')
elif count <= 10 and count > 5:
    print('Posees buen conocimiento general. Pero puede mejorar!')
elif count <= 15 and count > 10:
    print('Posees excelente conocimiento general')


