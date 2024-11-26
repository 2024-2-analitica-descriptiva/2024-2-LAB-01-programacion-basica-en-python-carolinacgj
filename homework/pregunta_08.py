"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]
    """
    values_by_key = {}

    with open("files/input/data.csv", "r") as file:
        for line in file:
            columns = line.strip().split("\t")
            column_0 = columns[0]  # Letra
            column_1 = int(columns[1])  # Valor numérico de la segunda columna

            # Asegurar que no se repitan las letras utilizando un conjunto
            if column_1 in values_by_key:
                values_by_key[column_1].add(column_0)  # Usar set para eliminar duplicados
            else:
                values_by_key[column_1] = {column_0}  # Inicializamos con un set

    # Convertir cada set en una lista ordenada
    result = [(key, sorted(list(value))) for key, value in sorted(values_by_key.items())]

    return result

# Código de prueba
if __name__ == "__main__":
    print(pregunta_08())
