from pilaE import PilaE
from pilaD import Pila
from colaE import ColaE
from colaD import ColaD
from colaCic import CircularQueue
from nodo import Nodo
from listaLigada import ListaLigada
from arboles import Nodos, Arbol



#----Menú principal----
# !TODO Preguntarle a rafa si se puede importar una clase que esta dentro de otra carpeta
print("\033[1;33m" + "¡Bienvenido al programa! \n" + "\033[0;m") #Esto es con código ANSI
menuPrincip = int(input(" 1-Ingresar datos \n 2-Salir \n Respuesta: ")) 
while menuPrincip != 2:
    #Ingresar los datos
    if menuPrincip == 1:
        datos = int(input ("Ingresa la cantidad de datos que quieres meter a tu lista: \n"))
        listaDatos = []
        for i in range (datos):
            dato = int(input("Ingresa tu dato:"))
            #Este primer append es válido para luego pasarlos a lo que el usuario requiera
            listaDatos.append(dato)
        print("Los datos que ingresaste son:", listaDatos)
        while True:
            estAusar = int(input("¿Con qué estructura de datos te gustaría trabajar? \n 1 - Pila Estática \n 2 - Pila Dinámica \n 3 - Lista Ligada \n 4 - Árboles \n 5 - Cola Estática \n 6 - Cola Dinámica \n 7 - Cola Circular \n 8 - Salir \n Respuesta: "))
            if estAusar == 8:
                break
            #Caso Pila Estática
            if estAusar == 1:
                pila = PilaE(len(listaDatos))
                for i in range (len(listaDatos)):
                    pila.push(listaDatos[i])
                pila.show()
                print("\n")
                while True:
                    decision = int(input("Escoge que quires hacer con tu pila \n 1 - Se mantiene así tu pila \n 2 - Añadir datos \n 3 - Quitar datos \n Respuesta: "))
                    if decision == 1:
                        print("Terminaste con tu pila!")
                        pila.show()
                        #Guardar los nuevos datos de la pila en la listaDatos
                        listaDatos =[]
                        while not pila.isEmpty():
                            listaDatos.append(pila.pop())
                        print ("La nueva lista de datos es: ", listaDatos)
                        break
                    if decision == 2:
                        if pila.isFull():
                            print("Tu pila está llena! \n")
                        else:
                            añadir= int(input("Inserta el número que se va a añadir: "))
                            pila.push(añadir)
                            pila.show()
                        # estAusar = int(input("¿Con qué estructura de datos te gustaría trabajar? \n 1 - Pila Estática \n 2 - Pila Dinámica \n 3 - Cola Estática \n 4 - Cola Dinámica \n 5 - Cola Circular \n 6 - Lista Ligada \n 7 - Árboles \n Respuesta: "))
                    else:
                        pila.pop()
                        print("\n")
                        pila.show() 
                        if pila.isEmpty():
                            print("Tu pila está vacía!")#Falta añadir un while para ver si el usuario quiere andar quitando o poniendo datos!!! Revisar!
                        #Go lightning McQueen!!!!!
                    
                        
            # Caso Pila Dinámica
            if estAusar == 2:
                pilaD = Pila()
                for i in range (len(listaDatos)):
                    pilaD.push(listaDatos[i])
                print("\n")
                pilaD.show()
                while True:
                    decision = int(input("Escoge qué quieres hacer con tu pila dinámica \n 1 - Se mantiene así tu pila \n 2- Añadir datos \n 3 - Quitar datos \n Respuesta: "))
                    if decision == 1:
                        print("Terminaste con tu pila! \n")
                        pilaD.show()
                        #Guardar los nuevo datos en listaDatos
                        while not pilaD.isEmpty():
                            listaDatos.append(pilaD.pop())
                        print("La nueva lista de datos es: ", listaDatos)
                        break
                    elif decision == 2:
                        añadir= int(input("Inserta el número que se va a añadir: "))
                        pilaD.push(añadir)
                        pilaD.show()
                        print("\n")
                    else:
                        pilaD.pop()
                        pilaD.show()
                        if pilaD.isEmpty():
                            print("Tu pila está vacía!")




            # #Caso Cola Estática
            if estAusar == 5:
                colaE = ColaE(len(listaDatos))
                for i in range (len(listaDatos)):
                    colaE.enqueue(listaDatos[i])
                colaE.mostrar()
                while True:
                    decision = int(input("Escoge qué quieres hacer con tu cola estática \n 1 - Se mantiene así tu cola \n 2- Encolar datos \n 3 - Desencolar datos \n Respuesta: "))
                    if decision == 1:
                        print("Terminaste con tu cola estática! \n")
                        print(f"Tu dato superior es: {colaE.top()}")
                        print(f"Tu dato inferor es: {colaE.last()} \n")
                        colaE.mostrar()
                        #Guardar los nuevo datos en listaDatos
                        listaDatos = []
                        while not colaE.is_empty():
                            listaDatos.append(colaE.dequeue())
                        print("La nueva lista de atos es: ", listaDatos)
                        break       
                    elif decision == 2:
                        if colaE.is_full():
                            print ("Tu cola estática está llena!")
                        else:
                            añadir = int(input("Inserta el número que se va a añadir: "))
                            colaE.enqueue(añadir)
                            colaE.mostrar()
                            print(f"Tu dato superior es: {colaE.top()}")
                            print(f"Tu dato inferor es: {colaE.last()} \n")    
                    else:
                        colaE.dequeue()
                        print("\n")
                        colaE.mostrar()
                        print(f"Tu dato superior es: {colaE.top()}")
                        print(f"Tu dato inferor es: {colaE.last()} \n")
                        if colaE.is_empty():
                            print("Tu cola está vacía!")
        

            # #Caso Cola Dinámica
            if estAusar == 6:
                colaD = ColaD()
                for i in range (len(listaDatos)):
                    colaD.enqueue(listaDatos[i])
                print("\n")
                colaD.show()
                while True:
                    decision = int(input("Escoge qué quieres hacer con tu Cola Dinámica \n 1 - Se mantiene así tu Cola \n 2- Encolar datos \n 3 - Desencolar datos \n Respuesta: "))
                    if decision == 1:
                        print("Terminaste con tu cola dinámica! \n")
                        print(f"Tu dato superior es: {colaD.front()}")
                        print(f"Tu dato inferior es: {colaD.last()} \n")
                        colaD.show()
                        #Guardar los nuevos datos en listaDatos
                        listaDatos = []
                        while not colaD.is_empty():
                            listaDatos.append(colaD)
                        print("La nueva lista de datos es: ", listaDatos)
                        break
                    elif decision == 2:
                        añadir= int(input("Inserta el número que se va a añadri: "))
                        colaD.enqueue(añadir)
                        colaD.show()
                        print("\n")
                        print(f"Tu dato superior es: {colaD.front()}")
                        print(f"Tu dato inferior es: {colaD.last()} \n")
                    else:
                        if not colaD.is_empty():
                            colaD.dequeue()
                            colaD.show()
                        print(f"Tu dato superior es: {colaD.front()}")
                        print(f"Tu dato inferior es: {colaD.last()} \n")
                        if colaD.is_empty():
                            print("Tu cola está vacía!")

                # #Caso Cola Circular
            if estAusar == 7:
                colaCirc = CircularQueue(len(listaDatos))
                for i in range(len(listaDatos)):
                    colaCirc.enqueue(listaDatos[i])
                colaCirc.display()
                print("\n")
                while True:
                    decision = int(input("Escoge que quires hacer con tu cola circular \n 1 - Se mantiene así tu cola circular \n 2 - Encolar datos \n 3 - Quitar datos \n Respuesta: "))
                    if decision == 1:
                        print("Terminaste con tu cola circular! \n")
                        colaCirc.display()
                        listaDatos = []
                        #Guardar los nuevos datos en listaDatos
                        while colaCirc:
                            listaDatos.append(colaCirc)
                        print("La nueva lista de datos es: ", listaDatos)
                        break
                    elif decision == 2: 
                        añadir = int(input("Inserta el número que se va a añadir:"))
                        colaCirc.enqueue(añadir)
                        colaCirc.display()
                        #estAusar = int(input("¿Con qué estructura de datos te gustaría trabajar? \n 1 - Pila Estática \n 2 - Pila Dinámica \n 3 - Cola Estática \n 4 - Cola Dinámica \n 5 - Cola Circular \n 6 - Lista Ligada \n 7 - Árboles \n Respuesta: "))
                    else:
                        colaCirc.dequeue()
                        print("\n")
                        colaCirc.display()


            
            #Caso Lista ligada
            if estAusar == 3:
                listaLig = ListaLigada()
                    
                print("\n")
                for i in range(len(listaDatos)):
                    nodo = Nodo(listaDatos[i])
                    decision = int(input(f"Quiere que el número {listaDatos[i]} lo pongamos al inicio? \n 1 - Si \n 2 - No \n Respuesta:"))
                    if decision == 1:
                        listaLig.insertar_inicio(nodo)
                    if decision == 2:
                        decision2 = int(input(f"Quieres que el número {listaDatos[i]} lo pongamos al final? \n 1 - Si \n 2 - No \n Respuesta:"))
                        if decision2 == 1:
                            listaLig.insertar_final(nodo)
                        if decision2 == 2:
                            posicion = int(input(f"Atrás de qué posición quieres colocar el número {listaDatos[i]}?"))
                            listaLig.insertar_posicion(nodo, posicion)
                    listaLig.mostrar()
            

                
            # #Arboles (Ծ‸ Ծ) carita de molesto grrrrrr
            if estAusar == 4:
                arbol = Arbol()
                for i in range(len(listaDatos)):
                    arbol.insertarNodo(listaDatos[i])
                decision = int(input("Ya ingresaste tus datos! Quieres ver el acomodamiento en: \n 1 - Anchura \n 2 - Pre-Orden \n 3 - Pos-Orden \n 4 - Inorden \n Respuesta:"))
                if decision == 1:
                    print("Tu árbol de anchura sería: \n")
                    arbol.anchura()
                    print("\n")
                elif decision == 2:
                    print("Tu árbol de pre-orden sería: \n")
                    arbol.pre_orden(arbol.raiz)
                    print("\n")
                elif decision == 3:
                    print("Tu árbol de Pos-orden sería: \n")
                    arbol.pos_orden(arbol.raiz)
                    print("\n")
                elif decision == 4:
                    print("Tu árbol de Inorden sería: \n")
                    arbol.inorden(arbol.raiz)
                    print("\n")
                     

            
        
    menuPrincip = int(input(" \n 1-Ingresar datos \n 2-Salir \n Respuesta: "))
print(" Fin del programa!")

