"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordenadas alfabéticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]
    """
    # Diccionario para acumular las sumas por letra
    sums_by_letter = {}

    # Leer el archivo línea por línea
    with open("files/input/data.csv", "r") as file:
        for line in file:
            # Dividir la línea en columnas usando tabulador como separador
            columns = line.split("\t")
            letter = columns[0]  # Primera columna (letra)
            value = int(columns[1])  # Segunda columna (número convertido a entero)

            # Sumar el valor al acumulador correspondiente en el diccionario
            if letter in sums_by_letter:
                sums_by_letter[letter] += value
            else:
                sums_by_letter[letter] = value

    # Ordenar el resultado alfabéticamente por letra y convertirlo en una lista de tuplas
    result = sorted(sums_by_letter.items())

    return result


# Código de prueba
if __name__ == "__main__":
    print(pregunta_03())
