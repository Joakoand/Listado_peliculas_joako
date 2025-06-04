# joaquin alberto andrada
#definimos la clase pelicula, para retornar cuando se den los nombres
class Pelicula:
    def __init__(self, nombre):
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre

    def __str__(self):
        return self.__nombre

# Variables para el menu de inicio
AGREGAR_PELICULA = 1
LISTAR_PELICULAS = 2
ELIMINAR_CATALOGO = 3
SALIR = 4

peliculas = []
opcion = 0

# Menu del catalogo
while opcion != SALIR:
    print("\n -Catálogo de Películas-")
    print(f"{AGREGAR_PELICULA}. Agregar Película")
    print(f"{LISTAR_PELICULAS}. Listar Películas")
    print(f"{ELIMINAR_CATALOGO}. Eliminar Catalogo")
    print(f"{SALIR}. Salir")

    try:
        opcion = int(input("Elige una opción: "))
    except ValueError:
        print("⚠️ Debes ingresar el número correspondiente a cada opcion.")
        continue

    #cuando pongo el numero 1, añado una pelicula.
    if opcion == AGREGAR_PELICULA:
        nombre = input("Ingrese el nombre de la película: ")
        nueva = Pelicula(nombre)
        peliculas.append(nueva)
        print(f"✅ Película '{nombre}' agregada.")
    #con el numero 2, muestra la lista de peliculas guardadas.
    elif opcion == LISTAR_PELICULAS:
        if peliculas:
            print("\n🎬 Películas en el catálogo:")
            for peli in peliculas:
                print(f"- {peli}")
       #si no hay nada muestra el siguiente mensaje
        else:
            print("⚠️ El catálogo está vacío.")
    #con el numero 3, eliminamos el catalogo.
    elif opcion == ELIMINAR_CATALOGO:
        peliculas.clear()
        print("🗑️ Catálogo eliminado.")
    #con el numero 4, salimos del codigo.
    elif opcion == SALIR:
        print("👋 Saliendo del programa. ¡Hasta pronto!")
    else:
        print("Opción inválida. Intenta de nuevo.")
