def analizar_dnis(dnis):
    """
    Analiza cada DNI por separado.
    - Cuenta la frecuencia de cada dígito.
    - Suma todos los dígitos.
    """

    print("\n--- Análisis de cada DNI ---")

    for dni in dnis:
        frecuencia = {}     # Diccionario para contar la frecuencia de cada dígito
        suma = 0    # Acumulador de la suma de dígitos

        for digito in dni:
            suma += int(digito)     # Se suma el valor del dígito como número
            frecuencia[digito] = frecuencia.get(digito, 0) + 1  # Cuenta cuántas veces aparece

        print(f"\nDNI: {dni}")
        print(f"\nFrecuencia de dígitos: {frecuencia}")
        print(f"\nSuma total de los dígitos: {suma}")


# --- Prueba rápida de la función ---
if __name__ == "__main__":
    dnis_prueba = ["12345678", "11223344", "87654321", "44448888", "00000001"]  # Lista de prueba de DNIs como strings
    analizar_dnis(dnis_prueba)  # Llamamos a la función con esta lista