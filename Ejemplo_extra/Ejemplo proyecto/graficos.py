import os


def exportar_grafo(filename="prueba.dot"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write("digraph G{")
 


def exportar_graphviz_tabla(estaciones, filename="matriz_tabla.dot"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write('digraph G {\n')
        f.write('fontname="Helvetica,Arial,sans-serif"\n')
        f.write('node [fontname="Helvetica,Arial,sans-serif"]\n')
        f.write('edge [fontname="Helvetica,Arial,sans-serif"]\n')
        f.write('a0 [shape=none label=<\n')
        f.write('<TABLE border="1" cellspacing="0" cellpadding="10">\n')

        # Encabezado
        f.write('<TR><TD></TD>')
        if estaciones.head and estaciones.head.sensores.head:
            actual_sensor = estaciones.head.sensores.head
            while actual_sensor:
                f.write(f'<TD bgcolor="lightgray"><B>s{actual_sensor.id_sensor}</B></TD>')
                actual_sensor = actual_sensor.siguiente
        f.write('</TR>\n')

        # Filas de estaciones y sensores
        actual_est = estaciones.head
        while actual_est:
            f.write(f'<TR><TD bgcolor="lightgray"><B>n{actual_est.id_estacion}</B></TD>')
            actual_sensor = actual_est.sensores.head
            while actual_sensor:
                valor = actual_sensor.valor
                
                # Asignar color basado en el valor
                if valor == 0:
                    color = "white"
                elif valor < 500:
                    color = "yellow"
                elif valor < 1000:
                    color = "yellow:orange"
                elif valor < 2000:
                    color = "orange"
                elif valor < 5000:
                    color = "orange:red"
                else:
                    color = "red"
                
                f.write(f'<TD bgcolor="{color}" gradientangle="315">{valor}</TD>')
                actual_sensor = actual_sensor.siguiente
            f.write('</TR>\n')
            actual_est = actual_est.siguiente

        f.write('</TABLE>>];\n')
        f.write('}\n')

def exportar_graphviz_matriz(estaciones, filename="matriz.dot"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write('digraph G {\n')
        f.write('    node [shape=box, width=1, height=0.6];\n')
        f.write('    graph [splines=false, nodesep=0.3, ranksep=0.6];\n\n')

        # Cabecera columnas (sensores)
        if estaciones.head and estaciones.head.sensores.head:
            actual_sensor = estaciones.head.sensores.head
            while actual_sensor:
                f.write(f'    s{actual_sensor.id_sensor} [label="s{actual_sensor.id_sensor}", shape=ellipse, style=filled, fillcolor=lightblue];\n')
                actual_sensor = actual_sensor.siguiente

        f.write('\n    // Cabecera filas (estaciones)\n')
        actual_est = estaciones.head
        while actual_est:
            f.write(f'    n{actual_est.id_estacion} [label="n{actual_est.id_estacion}", shape=ellipse, style=filled, fillcolor=lightgreen];\n')
            actual_est = actual_est.siguiente

        f.write('\n    // Matriz (nodo por celda con valor)\n')
        actual_est = estaciones.head
        while actual_est:
            actual_sensor = actual_est.sensores.head
            while actual_sensor:
                f.write(f'    n{actual_est.id_estacion}s{actual_sensor.id_sensor} [label="{actual_sensor.valor}"];\n')
                actual_sensor = actual_sensor.siguiente
            actual_est = actual_est.siguiente

        f.write('\n    // Alineación en filas\n')
        f.write('    {rank=same; vacio')
        if estaciones.head and estaciones.head.sensores.head:
            actual_sensor = estaciones.head.sensores.head
            while actual_sensor:
                f.write(f' s{actual_sensor.id_sensor}')
                actual_sensor = actual_sensor.siguiente
        f.write('}\n')

        actual_est = estaciones.head
        while actual_est:
            f.write(f'    {{rank=same; n{actual_est.id_estacion}')
            actual_sensor = actual_est.sensores.head
            while actual_sensor:
                f.write(f' n{actual_est.id_estacion}s{actual_sensor.id_sensor}')
                actual_sensor = actual_sensor.siguiente
            f.write('}\n')
            actual_est = actual_est.siguiente

        f.write('\n    // Conexiones horizontales\n')
        actual_est = estaciones.head
        while actual_est:
            f.write(f'    n{actual_est.id_estacion}')
            actual_sensor = actual_est.sensores.head
            while actual_sensor:
                f.write(f' -> n{actual_est.id_estacion}s{actual_sensor.id_sensor}')
                actual_sensor = actual_sensor.siguiente
            f.write(';\n')
            actual_est = actual_est.siguiente

        if estaciones.head and estaciones.head.sensores.head:
            f.write('    vacio')
            actual_sensor = estaciones.head.sensores.head
            while actual_sensor:
                f.write(f' -> s{actual_sensor.id_sensor}')
                actual_sensor = actual_sensor.siguiente
            f.write(' [style=invis];\n')

        f.write('\n    // Conexiones verticales invisibles para ordenar la matriz\n')
        f.write('    vacio')
        actual_est = estaciones.head
        while actual_est:
            f.write(f' -> n{actual_est.id_estacion}')
            actual_est = actual_est.siguiente
        f.write(' [style=invis];\n')

        if estaciones.head and estaciones.head.sensores.head:
            actual_sensor = estaciones.head.sensores.head
            while actual_sensor:
                f.write(f'    s{actual_sensor.id_sensor}')
                actual_est = estaciones.head
                while actual_est:
                    f.write(f' -> n{actual_est.id_estacion}s{actual_sensor.id_sensor}')
                    actual_est = actual_est.siguiente
                f.write(' [style=invis];\n')
                actual_sensor = actual_sensor.siguiente

        # Nodo invisible para esquina superior izquierda
        f.write('\n    vacio [label="", style=invis, width=0.1];\n')

        f.write('}\n')

def generar_imagen_dot(dotfile="matriz.dot", imgfile="matriz.png"):
    comando = f'dot -Tpng "{dotfile}" -o "{imgfile}"'
    resultado = os.system(comando)
    if resultado == 0:
        print(f"Imagen generada: {imgfile}")
    else:
        print("No se pudo generar la imagen. ¿Está instalado Graphviz y en el PATH?")


exportar_grafo()

        

