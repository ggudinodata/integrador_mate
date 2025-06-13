def verificar_grupo_z(anios):
    """
    Verifica si todos los integrantes nacieron despues del año 2000.
    """

    if all(anio > 2000 for anio in anios):
        print("Grupo Z: todos nacieron después del 2000.")
    else:
        print("No todos o ninguno pertenece al Grupo Z.")


# --- Prueba rápida de la función ---
if __name__ == "__main__":
    anios = [1992, 1994, 1987, 1999, 2002]
    verificar_grupo_z(anios)