Joaquin Alberto Andrada

import os

# Definimos la clase Pelicula, para representar cada película
class Pelicula:
    def __init__(self, nombre):
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre

    def __str__(self):
        return self.__nombre

# Variables para el menú de inicio
AGREGAR_PELICULA   = 1
LISTAR_PELICULAS   = 2
ELIMINAR_CATALOGO  = 3
SALIR              = 4

CATALOGO_ARCHIVO = "peliculas.txt"  # nombre del archivo que usaremos

# Función: cargar todas las películas que ya estén en "peliculas.txt"
def cargar_peliculas_desde_archivo():
    peliculas = []
    # Si el archivo no existe, devolvemos lista vacía
    if not os.path.exists(CATALOGO_ARCHIVO):
        return peliculas

    with open(CATALOGO_ARCHIVO, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            nombre = linea.strip()
            if nombre:
                peliculas.append(Pelicula(nombre))
    return peliculas

# Función: guardar la lista completa de películas en "peliculas.txt"
def guardar_peliculas_en_archivo(lista_peliculas):
    with open(CATALOGO_ARCHIVO, "w", encoding="utf-8") as archivo:
        for peli in lista_peliculas:
            archivo.write(peli.get_nombre() + "\n")

# Carga inicial: traemos del archivo cualquier película previa
peliculas = cargar_peliculas_desde_archivo()
opcion = 0

# Bucle del menú principal
while opcion != SALIR:
    print("\n -Catálogo de Películas-")
    print(f"{AGREGAR_PELICULA}. Agregar Película")
    print(f"{LISTAR_PELICULAS}. Listar Películas")
    print(f"{ELIMINAR_CATALOGO}. Eliminar Catálogo")
    print(f"{SALIR}. Salir")

    try:
        opcion = int(input("Elige una opción: "))
    except ValueError:
        print("⚠️ Debes ingresar el número correspondiente a cada opción.")
        continue

    #Opción 1: Agregar película
    if opcion == AGREGAR_PELICULA:
        nombre = input("Ingrese el nombre de la película: ").strip()
        if nombre:
            nueva = Pelicula(nombre)
            peliculas.append(nueva)
            guardar_peliculas_en_archivo(peliculas)
            print(f"✅ Película '{nombre}' agregada al catálogo (y guardada en {CATALOGO_ARCHIVO}).")
        else:
            print("⚠️ No ingresaste ningún nombre.")

    #Opción 2: Listar películas
    elif opcion == LISTAR_PELICULAS:
        if peliculas:
            print("\n🎬 Películas en el catálogo:")
            for peli in peliculas:
                print(f"- {peli}")
        else:
            print("⚠️ El catálogo está vacío (no hay películas en memoria).")

    #Opción 3: Eliminar catálogo
    elif opcion == ELIMINAR_CATALOGO:
        confirm = input("¿Seguro querés borrar TODO el catálogo? (s/n): ").strip().lower()
        if confirm == "s":
            # Si existe el archivo, lo borramos
            if os.path.exists(CATALOGO_ARCHIVO):
                os.remove(CATALOGO_ARCHIVO)
            # Limpiamos la lista en memoria también
            peliculas.clear()
            print(f"🗑️ Catálogo eliminado: se borró {CATALOGO_ARCHIVO} y la lista en memoria.")
        else:
            print("🔙 No se eliminó nada.")

    #Opción 4: Salir
    elif opcion == SALIR:
        print("👋 Saliendo del programa. ¡Hasta pronto!")

    #Opción inválida
    else:
        print("⚠️ Opción inválida. Intenta de nuevo.")
