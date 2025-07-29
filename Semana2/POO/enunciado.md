## Enunciado: Sistema de Gestión de Vehículos de una Agencia de Transporte
Una agencia de transporte necesita un sistema para gestionar sus vehículos. 
Existen distintos tipos de vehículos: automóviles particulares, camiones de carga, y motocicletas. Todos los vehículos tienen atributos comunes como: marca, modelo, año de fabricación y número de serie (privado).
Además:
•	Los automóviles pueden tener una propiedad adicional: número de puertas.
•	Los camiones de carga tienen un peso máximo de carga (en toneladas).
•	Las motocicletas indican si son eléctricas o no.
El sistema debe permitir:
1.	Crear distintos tipos de vehículos usando clases e herencia.
2.	Aplicar abstracción, definiendo una clase base abstracta Vehiculo con un método mostrar_informacion() que debe ser implementado por cada subclase.
3.	Usar encapsulamiento, manteniendo privado el número de serie y permitiendo su acceso solo mediante métodos get_numero_serie() y set_numero_serie().
4.	Aplicar polimorfismo, de modo que se pueda iterar sobre una lista de distintos vehículos y ejecutar el método mostrar_informacion() sin preocuparse del tipo específico de vehículo.
