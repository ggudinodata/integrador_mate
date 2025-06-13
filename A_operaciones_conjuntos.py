def operaciones_conjuntos(conjuntos):
    """
    Realiza operaciones entre conjuntos, dándole la posibilidad al usuario de seleccionar entre cuáles hacerlo:
    - Unión: todos los dígitos presentes en cualquier conjunto.
    - Intersección: dígitos presentes en todos los conjuntos.
    - Diferencia y diferencia simétrica entre los dos primeros conjuntos.
    """

    print("\n--- Operaciones de conjuntos ---")

    for i, conjunto in enumerate(conjuntos):    # Mostramos todos los conjuntos disponibles
        letra = chr(65 + i) # Convierte 0 → A, 1 → B, etc.
        print(f"{letra} {conjunto}")

    # Solicitamos al usuario que elija dos conjuntos
    entrada1 = input("Elija la letra del primer conjunto (ej. A): ").strip().upper()
    entrada2 = input("Elija la letra del segundo conjunto (ej. B): ").strip().upper()

    # Convertimos las letras a índices (A → 0, B → 1, etc.)
    indice1 = ord(entrada1) - 65
    indice2 = ord(entrada2) - 65

    # Verificamos que los índices ingresados sean válidos
    if indice1 not in range(len(conjuntos)) or indice2 not in range(len(conjuntos)):
        print("Error. Alguna de las letras ingresadas no corresponde a los conjuntos")
        return

    # Extraemos los conjuntos elegidos
    A = conjuntos[indice1]
    B = conjuntos[indice2]

    # Realizamos todas las operaciones
    union_AB = A | B # Unión: todos los elementos de ambos conjuntos usando desempaquetado (*conjuntos)
    interseccion_AB = A & B   # Intersección: elementos comunes a ambos conjuntos
    diferencia_AB = A - B     # Diferencia: A - B
    diferencia_BA = B - A     # Diferencia: B - A
    diferencia_sim_AB = A ^ B      # Diferencia simétrica: elementos que pertenecen a A o a B, pero no a ambos

    # Mostramos los resultados por consola
    print(f"\nConjunto {entrada1}: {A}")
    print(f"Conjunto {entrada2}: {B}")
    print(f"Unión {entrada1} ∪ {entrada2}: {union_AB}")
    print(f"Intersección {entrada1} ∩ {entrada2}: {interseccion_AB}")
    print(f"Diferencia {entrada1} - {entrada2}: {diferencia_AB}")
    print(f"Diferencia {entrada2} - {entrada1}: {diferencia_BA}")
    print(f"Diferencia simétrica {entrada1} Δ {entrada2}: {diferencia_sim_AB}")


if __name__ == "__main__":
    # Simulación de 5 DNIs ya convertidos en conjuntos
    conjuntos_prueba = [
        {1, 2, 3, 4, 5},       # Conjunto A
        {3, 4, 5, 6, 7},       # Conjunto B
        {1, 3, 5, 7, 9},       # Conjunto C
        {0, 2, 4, 6, 8},       # Conjunto D
        {2, 4, 6, 8, 9}        # Conjunto E
    ]


# --- Prueba rápida de la función ---
    print("Conjuntos de prueba:")
    for i, c in enumerate(conjuntos_prueba):
        print(f"Conjunto {chr(65+i)}: {c}")  # A, B, C...

    operaciones_conjuntos(conjuntos_prueba) # Llamamos a la función con los conjuntos simulados