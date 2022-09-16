import time
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

print (GREEN+ "Bienvenido a mi trivia que te pondra los pelos en punta "+RESET)
nombre_usuario = input("Digite su nombre: ")
puntaje = 30
print ("En cinco segundos iniciamos la trivia. PREPARATE!")
for numero_carga in range (5,0,-1):
  print(numero_carga)
  time.sleep(1)

print (BLUE+"Pondre a prueba tus conocimientos y obtendras un puntaje al finalizar la trivia " +RESET, nombre_usuario)
time.sleep(2)

print (GREEN+"Responder las siguientes preguntas escribiendo la letra de la alternativa correcta y presionando 'Enter' para enviar tu respuesta correcta:\n"+RESET)
time.sleep(2)
print(RED+"RECUERDA QUE SI FALLAS EN LAS RESPUESTAS TU PUNTAJE SE REDUCIRÁ"+RESET)
print("Tu puntaje inicial será", puntaje)
time.sleep(2)

print ("Pregunta 1")
print (YELLOW+"1) ¿Cuando es el dia del padre?\n"+ RESET)
print ("a) 25 de mayo")
print ("b) 19 de noviembre")
print ("c) 14 de agosto")
print ("d) 18 de junio")

respuesta1_usuario = input("\nTu respuesta: ")

while respuesta1_usuario not in ('a','b','c','d'):
  respuesta1_usuario = input("Para avanzar a la siguiente pregunta debes responder con las letras de las alternativas.")

print("lo verificaré")
time.sleep(2)

if respuesta1_usuario == 'a':
  print("Respuesta incorrecta", nombre_usuario)
  puntaje = puntaje - 2
  print("Tu puntaje es: ", puntaje)
elif respuesta1_usuario == 'b':
  print("Respuesta incorrecta", nombre_usuario)
  puntaje = puntaje - 2
  print("Tu puntaje es: ", puntaje)
elif respuesta1_usuario == 'c':
  print("Respuesta incorrecta", nombre_usuario)
  puntaje = puntaje - 2
  print("Tu puntaje es: ", puntaje)
else:
  puntaje = 30+2
  print ("Muy bien!", nombre_usuario)
  print ("Tienes:", puntaje , "puntos acumulados")
print (YELLOW+"\nPregunta 2"+RESET)
print ("¿Cuando es el dia de la madre?\n")
print ("a) 28 de mayo")
print ("b) 17 de noviembre")
print ("c) 11 de agosto")
print ("d) 1 de junio")

respuesta2_usuario = input("\nTu respuesta: ")

while respuesta2_usuario not in ('a','b','c','d'):
  respuesta2_usuario = input("Para avanzar a la siguiente pregunta debes responder con las letras de las alternativas.")

print("Dos segundos para evaluar tu respuesta, por favor.")
time.sleep(2)
if respuesta2_usuario == 'a':
  print("Respuesta incorrecta", nombre_usuario)
  puntaje = puntaje - 4
  print("Tu puntaje es: ", puntaje)
elif respuesta2_usuario == 'b':
  print("Respuesta incorrecta", nombre_usuario)
elif respuesta2_usuario == 'c':
  print("Respuesta incorrecta", nombre_usuario)
else:
  print ("Muy bien!", nombre_usuario)
  puntaje = 30 + 4
  print("Tienes:",puntaje,"acomulados")

print (YELLOW+"\nPregunta 3"+RESET)
print ("¿Cuando es el dia del niño?\n")
print ("a) 07 de mayo")
print ("b) 25 de noviembre")
print ("c) 21 de agosto")
print ("d) 19 de junio")

respuesta3_usuario = input("\nTu respuesta: ")

while respuesta3_usuario not in ('a','b','c','d'):
  respuesta3_usuario = input("Para avanzar a la siguiente pregunta debes responder con las letras de las alternativas.")

print("Dos segundos para verificar tu respuesta. Por favor") 
time.sleep(2)

if respuesta3_usuario == 'a':
  print("Respuesta incorrecta", nombre_usuario)
  puntaje = puntaje - 8
  print("Tu puntaje es: ", puntaje)  
elif respuesta3_usuario == 'b':
  print("Respuesta incorrecta", nombre_usuario)
elif respuesta3_usuario == 'd':
  print("Respuesta incorrecta", nombre_usuario)
else:
  print ("Muy bien!", nombre_usuario)
  puntaje = 30 + 8
  print(GREEN+"Tienes ",puntaje, "acumulados. Es la nota maxima. Felicidades!"+RESET)

print("******************************************")
print(GREEN+"Muchas gracias por participar en la trivia"+RESET)