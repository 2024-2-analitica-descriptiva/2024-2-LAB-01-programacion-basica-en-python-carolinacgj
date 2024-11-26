"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """

def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor después del carácter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado más
    pequeño y el valor asociado más grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]
    """
    # Diccionario para almacenar los valores de cada clave
    values_by_key = {}

    # Leer el archivo línea por línea
    with open("files/input/data.csv", "r") as file:
        for line in file:
            # Dividir la línea en columnas usando tabulador como separador
            columns = line.strip().split("\t")
            column_5 = columns[4]  # Obtener la columna 5

            # Separar los pares clave:valor
            pairs = column_5.split(",")
            for pair in pairs:
                key, value = pair.split(":")  # Dividir clave y valor
                value = int(value)  # Convertir el valor a entero

                # Actualizar el diccionario con los valores mínimo y máximo
                if key in values_by_key:
                    values_by_key[key].append(value)
                else:
                    values_by_key[key] = [value]

    # Calcular mínimo y máximo para cada clave
    result = []
    for key in sorted(values_by_key.keys()):
        min_value = min(values_by_key[key])
        max_value = max(values_by_key[key])
        result.append((key, min_value, max_value))

    return result


# Código de prueba
if __name__ == "__main__":
    print(pregunta_06())


