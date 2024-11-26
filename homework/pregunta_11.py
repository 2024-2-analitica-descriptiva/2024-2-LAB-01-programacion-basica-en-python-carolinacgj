"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    values_by_letter = {}

    # Leer el archivo línea por línea
    with open("files/input/data.csv", "r") as file:
        for line in file:
            # Dividir la línea en columnas usando tabulador como separador
            columns = line.strip().split("\t")
            columns_1 = int(columns[1]) 
            columns_3 = columns[3].split(",")

            for i in columns_3:
                if i in values_by_letter:
                    values_by_letter[i]+=columns_1
                else:
                    values_by_letter[i] = columns_1

    return dict(sorted(values_by_letter.items()))

# Código de prueba
if __name__ == "__main__":
    print(pregunta_11())