# Sistema de Gestión de Bibliotecas

Este proyecto tiene como objetivo desarrollar un sistema de gestión para bibliotecas que permita organizar libros, estanterías y sucursales de manera eficiente. El sistema utiliza estructuras de datos enlazadas para modelar las relaciones entre estos elementos.

## Funcionalidades Principales

### 1. Gestión de Libros
- **Descripción**: Los libros son los elementos básicos del sistema. Cada libro tiene un título y un autor.
- **Estructura**: Los libros se almacenan en una lista enlazada simple.
- **Operaciones**:
  - **Agregar libro**: Permite añadir un nuevo libro a la lista.
  - **Mostrar libros**: Muestra todos los libros en la lista de manera organizada.
  - **Eliminar libro**: Permite eliminar un libro de la lista por su título.

### 2. Gestión de Estanterías
- **Descripción**: Las estanterías son contenedores de libros. Cada estantería tiene un número, un código y una lista de libros asociada.
- **Estructura**: Las estanterías se almacenan en una lista doblemente enlazada.
- **Operaciones**:
  - **Agregar estantería**: Permite añadir una nueva estantería a la lista.
  - **Mostrar estanterías**: Muestra todas las estanterías junto con los libros que contienen.
  - **Eliminar estantería**: Permite eliminar una estantería de la lista por su número.

### 3. Gestión de Sucursales
- **Descripción**: Las sucursales representan las ubicaciones físicas de las bibliotecas. Cada sucursal tiene un nombre, una dirección y una lista de estanterías asociada.
- **Estructura**: Las sucursales se almacenan en una lista circular enlazada.
- **Operaciones**:
  - **Agregar sucursal**: Permite añadir una nueva sucursal a la lista.
  - **Mostrar sucursales**: Muestra todas las sucursales junto con las estanterías y libros que contienen.
  - **Eliminar sucursal**: Permite eliminar una sucursal de la lista por su nombre.

## Detalles Técnicos

### Estructuras de Datos
1. **Lista Enlazada Simple**:
   - Utilizada para almacenar libros.
   - Cada nodo contiene un libro y un puntero al siguiente nodo.

2. **Lista Doblemente Enlazada**:
   - Utilizada para almacenar estanterías.
   - Cada nodo contiene una estantería, un puntero al nodo siguiente y un puntero al nodo anterior.

3. **Lista Circular Enlazada**:
   - Utilizada para almacenar sucursales.
   - Cada nodo contiene una sucursal y un puntero al nodo siguiente. El último nodo apunta al primero.

### Manejo de Casos Especiales
- Si una lista está vacía, los métodos de mostrar y eliminar deben manejar este caso mostrando mensajes adecuados.
- Los métodos de eliminación deben buscar el elemento por su identificador (título, número o nombre) y eliminarlo si existe.

## Ejemplo de Uso
1. Crear una lista de libros y agregar libros a ella.
2. Crear una lista de estanterías y asociar listas de libros a las estanterías.
3. Crear una lista de sucursales y asociar listas de estanterías a las sucursales.
4. Mostrar las sucursales, estanterías y libros organizados.
5. Eliminar un libro, una estantería o una sucursal y verificar los cambios.

Este sistema permite gestionar de manera eficiente los recursos de una biblioteca, facilitando la organización y el acceso a la información.