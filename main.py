import random
import time

intentos = 3
lugarActual = int(0)
incognita = 0
errores = 0
maximo = 0

## Texto introductorio al juego con modulo time.
def introduccion():
    print('A continuacion vamos a jugar una adivinanza.\n')
    time.sleep(2)
    print('Vas a tener que escribir un número entre 1 y 9, que será igual la cantidad de números que deberás adivinar (Mientras más grande el número, más difícil de adivinar).\n')
    time.sleep(3)
    print('Luego deberas escribir números para acertar la incognita. Podes equivocarte hasta', intentos, 'veces. Si fallas, perderás.\n')
    time.sleep(2)
    print('¡Buena suerte!\n')


## Funcion que solicita al jugador el largo del número incognita, que luego se va a generar con la funcion generarNumero()
def pedirCadena():
    global incognita
    cadena = int(input('Escribi la longitud de la cadena (1 a 5 dígitos):'))
    if (cadena < 1 or cadena > 5):
        print('La longitud de la cadena debe ser entre 1 y 5 digitos.')
        pedirCadena()
    else:
        incogita = generarNumero(cadena)

## Funcion que genera el número incognita a partir del largo introducido por el usuario en la funcion pedirCadena()
def generarNumero(length):
    global incognita, maximo
    generados = 0
    numFinal = ''
    while generados < length:
        nuevoNum = str(random.randint(0, 9))
        generados += 1
        numFinal = numFinal + nuevoNum
        incognita = numFinal
        maximo = length

## Funcion que verifica los intentos que tenemos y la posición del número buscado.
def pedirDigito():
    global errores, intentos, lugarActual
    if (errores >= intentos):
        return print('Agotaste todos los intentos y no adivinaste la incognita (', incognita, ')')
    else:
        if lugarActual < maximo:
            num = int(input('Escribí un número: '))
            if num is None:
                print('No has escrito ningún número.')
                pedirDigito()
            elif num < 0 or num > 9:
                print('El número debe estar entre 0 y 9.')
                pedirDigito()
            else:
                verificarDigito(num)
        elif lugarActual >= maximo:
            print('¡Ganaste el juego!\nAcertaste la incognita que era:', incognita)


## Funcion que compara el dígito ingresado por el usuario con el dígito de la incognita y devuelve el resultado.
def verificarDigito(numero):
    global lugarActual, errores, incognita
    if (str(numero) != incognita[lugarActual]):
        print('¡Número incorrecto! [ Errores actuales:', errores + 1, ']')
        errores = errores + 1
        pedirDigito()
    elif (str(numero) == incognita[lugarActual]):
        lugarActual = lugarActual + 1
        print('¡Número correcto!')
        pedirDigito()



introduccion()
pedirCadena()
pedirDigito()