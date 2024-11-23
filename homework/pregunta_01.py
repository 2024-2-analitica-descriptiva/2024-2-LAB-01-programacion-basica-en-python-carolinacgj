"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    suma=0
    with open(r"C:\Users\DELL\OneDrive\Escritorio\Especialización\Analitica Descriptiva\2024-2-LAB-01-programacion-basica-en-python-carolinacgj\files\input\data.csv", "r") as file:
        for line in file:
            columns=line.strip().split("\t")
            suma+=int(columns[1])
    return suma


print(pregunta_01())


