    for pregunta, respuesta_correcta in afirmaciones.items():
        print('\nVerdadero o falso?: ', pregunta)

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
        else:
            respuesta_texto = 'verdadero' if respuesta_correcta else 'false'
            print(f'La respuesta correcta es {respuesta_texto}!') 