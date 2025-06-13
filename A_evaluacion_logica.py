def evaluar_logica(conjuntos):
    """
    Evalúa condiciones lógicas:
    - Si todos los conjuntos tienen al menos 5 elementos, entonces hay alta diversidad numérica.
    - Si la intersección de todos los conjuntos tiene exactamente un elemento, ese es el dígito representativo del grupo.
    """

    print("\n--- Evaluación de condiciones lógicas ---")

    cinco_o_mas = all(len(conjunto) >= 5 for conjunto in conjuntos)     # Verificamos si TODOS los conjuntos tienen 5 o mas dígitos únicos
    if cinco_o_mas:
        print("Alta diversidad numérica, todos los conjuntos tiene 5 o más dígitos únicos.")
    else:
        print("No hay alta diversidad numérica.")


    interseccion_total = set.intersection(*conjuntos)   # Calculamos la intersección total entre TODOS los conjuntos
    if len(interseccion_total) == 1:
        digito_representativo = list(interseccion_total)[0]
        print(f"El dígito representativo del grupo es: {digito_representativo}")
    else:
        print("El grupo no tiene dígito representativo.")


# --- Prueba rápida de la función ---
if __name__ == "__main__":
    conjuntos_prueba = [
        {1, 3, 5, 7, 9},
        {0, 2, 4, 5, 6},
        {5, 8, 10, 11, 12},
        {5, 13, 14, 15, 16},
        {5, 17, 18, 19, 20}
    ]
    evaluar_logica(conjuntos_prueba)
