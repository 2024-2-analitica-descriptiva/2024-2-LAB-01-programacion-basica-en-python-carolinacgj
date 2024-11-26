
def pregunta_05():
    """
    Retorne una lista de tuplas con el valor máximo y mínimo de la columna 2
    por cada letra de la columna 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]
    """
    # Diccionario para almacenar los valores por letra
    values_by_letter = {}

    # Leer el archivo línea por línea
    with open("files/input/data.csv", "r") as file:
        for line in file:
            # Dividir la línea en columnas usando tabulador como separador
            columns = line.strip().split("\t")
            letter = columns[0]  # Primera columna (letra)
            value = int(columns[1])  # Segunda columna (número convertido a entero)

            # Agregar el valor a la lista correspondiente a la letra
            if letter in values_by_letter:
                values_by_letter[letter].append(value)
            else:
                values_by_letter[letter] = [value]

    # Calcular el máximo y mínimo por cada letra
    result = []
    for letter, values in sorted(values_by_letter.items()):
        max_value = max(values)
        min_value = min(values)
        result.append((letter, max_value, min_value))

    return result


# Código de prueba
if __name__ == "__main__":
    print(pregunta_05())
