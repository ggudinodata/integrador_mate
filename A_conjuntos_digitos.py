def crear_conjuntos_digitos(dnis):
    """
    A partir de cada DNI, genera un conjunto de dígitos unicos.
    Los dígitos se convierten en enteros para trabajar con conjuntos de números.
    """

    conjuntos = []  # Creamos una lista vacía para guardar los conjuntos
    for dni in dnis:
        conjunto = set(int(d) for d in dni)     # Convertimos cada caracter en entero y lo metemos en un set
        conjuntos.append(conjunto)      # Se agrega el conjunto a la lista
    return conjuntos    # Devuelve la lista de conjuntos


# --- Prueba rápida de la función ---
if __name__ == "__main__":
    dnis_de_prueba = ["12345678", "87654321", "11223344", "55667788", "12344321"]       # Lista de prueba

    conjuntos = crear_conjuntos_digitos(dnis_de_prueba)     # Llamamos a la función con esta lista

    print("Conjuntos de dígitos únicos por DNI:")       # Mostramos los conjuntos generados
    for i, conjunto in enumerate(conjuntos):
        print(f"DNI {i+1} ({dnis_de_prueba[i]}): {conjunto}")