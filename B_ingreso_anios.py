from datetime import date

def ingresar_anios():
    """
    Solicita al usuario ingresar 5 años de nacimiento (uno por cada integrante del grupo).
    Devuelve una lista con los años ingresados como enteros.
    """

    anios = []
    while len(anios) < 5:
        entrada = input(f"Ingrese el año de nacimiento del integrante {len(anios) + 1}: ")
        if entrada.isdigit() and 1900 <= int(entrada) <= date.today().year:
            anios.append(int(entrada))
        else:
            print("Año inválido. Debe ser numérico y real (entre 1900 y año actual).")
        
    return anios


# --- Prueba rápida de la función ---
if __name__ == "__main__":
    anios = ingresar_anios()
    print("Años ingresados:", anios)