"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """
    sums_by_month = {}

    # Leer el archivo línea por línea
    with open("files/input/data.csv", "r") as file:
        for line in file:
            # Dividir la línea en columnas usando tabulador como separador
            columns = line.split("\t")
            date = columns[2]  # toma la columna fecha
            month=date.split("-")[1] #divide la fecha por - y toma el dato mes
            

            # Sumar el valor al acumulador correspondiente en el diccionario
            if month in sums_by_month:
                sums_by_month[month] += 1
            else:
                sums_by_month[month] = 1

    # Ordenar el resultado alfabéticamente por letra y convertirlo en una lista de tuplas
    result = sorted(sums_by_month.items())

    return result


# Código de prueba
if __name__ == "__main__":
    print(pregunta_04())
