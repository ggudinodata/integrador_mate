def contar_pares_impares(anios):
    """
    Cuenta cuántos años son pares e impares.
    Imprime los resultados.
    """

    # Inicializamos los contadores en 0
    pares = 0
    impares = 0

    for anio in anios:
        if anio % 2 == 0:   # Verificamos si el número es par, en caso de ser así, aumentamos el contador en 1
            pares += 1
        else:
            impares += 1    # De lo contrario, aumentamos en 1 el contador de los impares
    
    # Imprimimos por pantalla los resultados
    print(f"Años pares: {pares}")
    print(f"Años impares: {impares}")


# --- Prueba rápida de la función ---
if __name__ == "__main__":
    anios = [1992, 1994, 1987, 1999, 2002]
    contar_pares_impares(anios)