sentence = 'Hola mundo'

print(sentence[0])

print (sentence[:])

print(sentence[2:])

print(sentence[:3])

print(sentence[2:5])

print(sentence[1:8:3])

'mundo' in sentence

game = 'piedra-papel-tijera'

type(game.split('-'))

serial_number = '\n\t \n 48374983274832 \n\n\t \t \n'

serial_number.strip()

#A continuación vamos a hacer «limpieza» por la izquierda (comienzo) y por la derecha (final)
#utilizando la función lstrip() y rstrip() respectivamente:
serial_number.lstrip()
serial_number.rstrip()
#Como habíamos comentado, también existe la posibilidad de especificar los caracteres que
#queremos borrar:
serial_number.strip('\n')
    
lyrics = '''Quizás porque mi niñez
... Sigue jugando en tu playa
... Y escondido tras las cañas
... Duerme mi primer amor
... Llevo tu luz y tu olor
... Por dondequiera que vaya'''
lyrics.startswith(' Quizás' )
lyrics.count( 'mi' )

proverb = 'Quien mal anda mal acaba'

proverb.replace('mal','bien')

proverb.replace('mal','bien',1)

x = 10
f'The variable is {{ x = {x} }}'

value = 0b10010011

f'{value}'
f'{value:b}'



text = "abc\ndef"
print(text)

text= r'abc\ndef'
print(text)