# Juego de afirmaciones     

afirmaciones = {
    'Sin fuego no hay humanidad tal como la conocemos' : True,
    'En 1776 las 13 colonias britanica declararon su independencia conformando lo que es hoy USA' : True,
    'Cristobal Colon llego al continente americano en 1493' : False,
    'El imperio romano fue uno de los mas influyentes en la historia': True,
    'La caida del muro de berlin no reunifico alemania': False
}
# Recorremos las afirmaciones

for pregunta, respuesta_correcta in afirmaciones.items():
    print('Verdadero o falso?: ', pregunta)

    # Le preguntamos al usuario por su respuesta
    respuesta_usuario = input('Ingresa "verdadero" o "falso": ').strip().lower()

    # Transformamos las respuestas a booleanos
    if respuesta_usuario == 'verdadero':
      respuesta_usuario_bool = True
    elif respuesta_usuario == 'falso':
      respuesta_usuario_bool = False
    else:
      print('Debes ingresar "verdadero" o "falso".')
      continue  # Continua la siguiente pregunta

    # Hacemos un codigo que evalue la respuesta del usuario y que coincida con la respuesta real

    if respuesta_usuario_bool == respuesta_correcta:
      print('Correcto!')
    else:
      respuesta_texto = 'Verdadero' if respuesta_correcta else 'falso'
      print(f'Oops! La respuesta correcta es {respuesta_texto}')
    



