def ingresar_dnis():
    """
    Solicita 5 DNIs al usuario. Cada uno debe tener exactamente 8 dígitos numéricos.
    Los DNIs se guardan en una lista
    """
    dnis = []   # Creamos una lista vacía para guardar los DNIs
    while len(dnis) < 5:    # Se repite hasta tener 5 DNIs válidos
        dni = input(f"Ingresá el DNI {len(dnis)+1} (8 dígitos numéricos): ")    # Solicitamos que el usuario ingrese los DNIs
        if dni.isdigit() and len(dni) == 8:  # Verificamos que el dato ingresao sea numérico y tenga 8 dígitos   
            dnis.append(dni) # En caso de ser válido, lo agregamos a la lista
        else:
            print("Error: el DNI debe ser numérico y tener exactamente 8 dígitos.") 
    return dnis # Devuelve la lista de DNIs


# --- Prueba rápida de la función ---
if __name__ == "__main__":
    dnis = ingresar_dnis()
    print("Lista de DNIs ingresados:", dnis)