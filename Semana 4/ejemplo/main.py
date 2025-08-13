from libros import Libro, ListaLibros
from estanteria import Estanteria, ListaEstanterias
from sucursales import Sucursal, ListaSucursales


libros_1 = ListaLibros()
libros_1.append(Libro("El Quijote", "Miguel de Cervantes"))
libros_1.append(Libro("Cien Años de Soledad", "Gabriel García Márquez"))
libros_1.append(Libro("1984", "George Orwell"))

libros_2 = ListaLibros()
libros_2.append(Libro("La Sombra del Viento", "Carlos Ruiz Zafón"))
libros_2.append(Libro("Donde los Árboles Cantan", "Laura Gallego"))
libros_2.append(Libro("El Juego del Ángel", "Carlos Ruiz Zafón"))

libros_3 = ListaLibros()
libros_3.append(Libro("Fahrenheit 451", "Ray Bradbury"))
libros_3.append(Libro("El Nombre del Viento", "Patrick Rothfuss"))
libros_3.append(Libro("El Principito", "Antoine de Saint-Exupéry"))

libros_4 = ListaLibros()
libros_4.append(Libro("El Hobbit", "J.R.R. Tolkien"))
libros_4.append(Libro("Moby Dick", "Herman Melville"))
libros_4.append(Libro("Orgullo y Prejuicio", "Jane Austen"))

# Creación de estanterías
estanterias_1 = ListaEstanterias()
estanterias_1.append(Estanteria("Estantería 1", "C01", libros_1))
estanterias_1.append(Estanteria("Estantería 2", "C02", libros_2))

estanterias_2 = ListaEstanterias()
estanterias_2.append(Estanteria("Estantería 3", "C03", libros_3))
estanterias_2.append(Estanteria("Estantería 4", "C04", libros_4))

# Creación de sucursales
sucursales_1 = ListaSucursales()
sucursales_1.append(Sucursal("Sucursal 1", "Calle 1", estanterias_1))
sucursales_1.append(Sucursal("Sucursal 2", "Calle 2", estanterias_2))

sucursales_1.mostrar_sucursales()



