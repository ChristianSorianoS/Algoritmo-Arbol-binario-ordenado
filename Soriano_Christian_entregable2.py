
#Se definen las variables y se dejan vacías
class libro():
    def __init__(self, id=None, titulo=None, autor=None, anio=None, izq=None, der=None):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.izq = izq
        self.der = der

#Se define la clase arbol
class arbol():
    def __init__(self):
        self.raiz = None

#Se definen las opciones del menú
    #Inserta los nodos a la izquierda si es menor y a la derecha si es mayor
    def insertar(self, a, libro):
        if a == None:
            a = libro
        else:
            d = a.id
            if libro.id < d:
                a.izq = self.insertar(a.izq, libro)
            else:
                a.der = self.insertar(a.der, libro)
        return a

#Ordena el arbol de forma "preorden"
    def preorden(self, a):
        if a == None:
            return None
        else:
            print(f'{a.id} ', end='')
            self.preorden(a.izq)
            self.preorden(a.der)

#Busca el nodo mediante el número ID,si es menor a la izquierda y si es mayor a la derecha
    def buscar(self, id, a):
        if a == None:
            return None
        else:
            if id == a.id:
                return a
            else:
                if id < a.id:
                    return self.buscar(id, a.izq)
                else:
                    return self.buscar(id, a.der)
arbol = arbol()

#Menú y salida de datos
while True:
    print("\nEJERCICIO ARBOL BINARIO ORDENADO EN PREORDEN")
    opc = input(
        "\n1.-Insertar libro (nodo) (Ejemplo formato: 251982,El leon la bruja y el ropero,C.S. Lewis,1950)\n2.-Mostrar ID arbol ordenado Preorden \n3.-Buscar libro por ID \n4.-Cerrar programa \n\nSeleccione una opcion del menú ---> ")

    if opc == '1':
        try:
            lib = input("ingrese el libro (id,titulo,autor,año)--> ")
            #Acá separa los datos mediante las comas para darle a cada variable su valor
            separar = lib.split(",")
            id = int(separar[0])
            titulo = str(separar[1])
            autor = str(separar[2])
            anio = int(separar[3])
            print("Libro ingresado! Código:", id, "| Titulo:", titulo, "| Autor:", autor, "| Año:", anio)
            nodo = libro(id, titulo, autor, anio)
            arbol.raiz = arbol.insertar(arbol.raiz, nodo)
        except IndexError:
            print ("Favor ingrese el libro según la codificación indicada (id,titulo,autor,año)")
        except ValueError:
            print ("Favor ingrese el libro según la codificación indicada (id,titulo,autor,año)")

    elif opc == '2':
        if arbol.raiz == None:
            print("El arbol se encuentra vacio, favor ingrese libro(s)")
        else:
            arbol.preorden(arbol.raiz)

    elif opc == '3':
        nodo = input("\nIngrese el id del libro (nodo) que desea buscar ---> ")
        if nodo.isdigit():
            nodo = int(nodo)
            if arbol.buscar(nodo, arbol.raiz) == None:
                print("\nId Libro (nodo) no encontrado (False)")
            else:
                l = arbol.buscar(nodo, arbol.raiz)
                print(f'Libro (nodo) encontrado ---> Titulo:{l.titulo} | Autor:{l.autor} | Año:{l.anio}')
        else:
            print("\nNo ingresó un Id valido, regresamos al menú principal")

    elif opc == '4':
        print("\nPrograma finalizado!!!\n")
        break
    else:
        print("\nElige una opcion que se encuentre en el menú (1-5)")

