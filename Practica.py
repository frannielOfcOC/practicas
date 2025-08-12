#primero agregar una biblioteca de mobs
#segundo agregar una lista de mobs vacia para ir agregandolos
#tercero crear 3 funciones, de: generar mobs (alealtoriamente), ver mobs activos y atacar.
#cuarto, implementar una funcion menu que se encargarar de llamar a las otras funciones
#segun el numero que le correspondan, por ejemplo 1, llama a la funcion de respawnear mob y agregarlo a esa lista.



import random #lo usaremos mas adelante

MOBS = {"E": "esqueleto",
         "Z" : "zombie",
           "G" : "globin"} #biblioteca de mobs
lista_mobs_spawn = [] #lista para almacenar esos mobs (no cambiar valor o agregar)

def generar_mobs(): #primera funcion
 Random_mob = random.choice(list(MOBS)) #Selecciona un mob random de la biblioteca de mobs y lo convierte a lista
 lista_mobs_spawn.append(Random_mob) #mandamos la lista de mob alealtoria a la variable mobs spawn vacia
 print("UN", lista_mobs_spawn, MOBS [Random_mob], "SALVAJE APARECIO!!!!!") #llamamos a la biblioteca mobs y especificamos que escoja la variable seleccionada ramdon


def mobs_activos(): # funcion para ver mobs activos 
 print (lista_mobs_spawn)

def atacar_mobs(): # un poco mas complicado pero sencillo, basicamente la funcion de atacar, que en este caso elimina los elementos almacenados en la lista de mobs activos
 atacar = input ("precione la letra A para atacar: ") # llamamos al usuario para que ataque con la letra A, le podemos agregar un replace para arreglar el problema de las mayusculas o minusculas.
 if atacar == "A":
  Mobs_eliminados = lista_mobs_spawn.pop() #elimina el ultimo mob que aparecio.
  print ("haz eliminado al enemigo: ", MOBS [Mobs_eliminados])
 else:
  print ("Letra incorrecta: ")
  return atacar_mobs()

Reinicio = False 
while Reinicio != True:
 print ("Inicio del super gameplay con graficos AAA")
 print("opcion 1: generar mobs")
 print("opcion 2: ver mobs activos")
 print("opcion 3: atacar mobs")
 Menu = input ("Porfavor seleccione una opcion: ")

 if Menu == "1":
  generar_mobs()

 if Menu == "2":
  mobs_activos()

 if Menu == "3":
  atacar_mobs()

 if Menu == "4":
  Reinicio = True
 else:
  print("seleccione una opcion")

