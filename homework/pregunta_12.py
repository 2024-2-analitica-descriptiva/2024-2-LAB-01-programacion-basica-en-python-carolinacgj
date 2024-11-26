"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}
    """
    values_by_letter = {}

    # Leer el archivo línea por línea
    with open("files/input/data.csv", "r") as file:
        for line in file:
            # Dividir la línea en columnas usando tabulador como separador
            columns = line.strip().split("\t")
            column_0 = columns[0]  # Columna 1 (letra)
            column_4 = columns[4]  # Columna 5 (valor en formato clave:valor)

            # Dividir la columna 5 en pares clave-valor
            pairs = column_4.split(",")
            
            # Inicializar la variable que llevará la suma de los valores
            total = 0
            
            # Sumar los valores de la columna 5 (separados por comas)
            for pair in pairs:
                key, value = pair.split(":")  # Separar la clave del valor
                total += int(value)  # Sumar el valor a la variable total
            
            # Agregar el total al diccionario, sumando si ya existe la clave
            if column_0 in values_by_letter:
                values_by_letter[column_0] += total
            else:
                values_by_letter[column_0] = total

    # Ordenar el diccionario por la clave y devolverlo
    return dict(sorted(values_by_letter.items()))

# Código de prueba
if __name__ == "__main__":
    print(pregunta_12())
