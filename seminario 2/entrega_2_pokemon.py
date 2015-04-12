#GRUPO 4
#Juan Manuel Hidalgo Navarro
#Alexandra Moron Mendez

#Programa que cuenta la cadena de nombres de pokemos concatenados por su primera y ultima letra.

f = open("pokemon.txt", 'r')
texto = f.read()
texto = texto.replace("\n", ' ')   #Quitar el caracter \n
texto = texto.replace("\xef", ' ') #Quitar el caracter \xef
texto = texto.replace("\xbb", ' ') #Quitar el caracter \xbb
texto = texto.replace("\xbf", ' ') #Quitar el caracter \xbf
lista = texto.split()

max_palabras = 0

for i in range(len(lista)):
    num_palabras = 0                        #Inicializamos a 0 el numero de palabras que hemos seleccionado
    palabra = lista[i]                      #Busca la palabra i-esima
    ultima_letra = palabra[len(palabra)-1]  #Coge la ultima letra de la palabra i-esima
    lista_aux = []                          #Creamos una lista auxiliar para introducir las palabras seleccionadas
    lista_aux.insert(num_palabras, palabra) #Introducimos la palabra seleccionada
    num_palabras = 1                        #Ponemos a 1 el numero de palabras seleccionada
    k = 0
    #Recorremos de nuevo la lista buscando una posible siguiente palabra
    #Restringimos que la palabra empiece por la ultima letra de la anterior y que no este en la lista de seleccionadas
    while (k < len(lista)):
        if(lista[k][0] == ultima_letra and not lista[k] in lista_aux):
            palabra = lista[k]                       #Guardamos la palabra k-esima de la lista
            ultima_letra = lista[k][len(palabra)-1]  #Obtenemos la ultima letra de la nueva palabra
            lista_aux.insert(num_palabras, lista[k]) #La insertamos en nuestra lista de palabras seleccionadas
            num_palabras = num_palabras + 1          #Incrementamos el numero de palabras seleccionadas
            k = 0                                    #Y ponemos a cero la variable k para que vuelva a recorrer la lista
        else:
            k = k + 1   #Si la palabra k-esima no cumple las restricciones, pasamos a la siguiente
        
    if num_palabras >= max_palabras: #Si el numero de palabras es mayor que el maximo...
        max_palabras = num_palabras  #Se actualiza el maximo numero de palabras
        lista_final = lista_aux      #Se actualiza la lista con el mayor numero de palabras
    
    
print "El numero maximo de nombres concatenados es: ", max_palabras, "\n",lista_final

