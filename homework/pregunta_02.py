"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
    # Generar lista con las lineas de data
    letter_count=[]
    with open("files\input\data.csv", "r") as file:
        lines=file.readlines()
    
    # Agregamos la primera columna de cada linea a letter_count = mapper (mapreduce)
    for line in lines:
        letter_count.append(((line.split("\t")[0]),1))

     # Odenamos alfabeticamento por clave letter_count = shuffle_and_sort (mapreduce)
    letter_count= sorted(letter_count, key=lambda x: x[0])

    #Sumamos la aparicion = Reduce (mapreduce)

    diccionario = {}

    for key, value in letter_count:
        if key in diccionario:
            diccionario[key] += value
        else:
            diccionario[key] = value
    return list(diccionario.items())
    

if __name__ == "__main__":
    print(pregunta_02())

