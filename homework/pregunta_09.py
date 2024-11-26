"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

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
                value = int(1)  # Convertir el valor a entero

                # Actualizar el diccionario con los valores mínimo y máximo
                if key in values_by_key:
                    values_by_key[key]+=value
                else:
                    values_by_key[key] = value

    # Calcular mínimo y máximo para cada clave


    return dict(sorted(values_by_key.items()))

# Código de prueba
if __name__ == "__main__":
    print(pregunta_09())

