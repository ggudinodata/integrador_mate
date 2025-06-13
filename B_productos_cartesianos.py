def producto_cartesiano(anios, edades):
    """
    Calcula el producto cartesiano entre los años de nacimiento y las edades actuales.
    Muestra los pares ordenados (año, edad).
    """

    pares = [(anio, edad) for anio in anios for edad in edades]
    print("Producto cartesiano (año, edad):")
    print(pares)

# --- Prueba rápida de la función ---
if __name__ == "__main__":
    anios = [1992, 1994, 2002]
    edades = [33, 31, 23]
    producto_cartesiano(anios, edades)
