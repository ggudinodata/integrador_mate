def verificar_bisiestos(anios):
    """
    Verifica si al menos uno de los años ingresados es bisiesto.
    Un año es bisiesto si es divisible por 4,
    pero no por 100, salvo que también sea divisible por 400.
    """

    # Evaluamos si algun año es bisiesto
    hay_bisiesto = any(
        (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)
        for anio in anios
    )

    if hay_bisiesto:
        print("Tenemos un año especial. Al menos un integrante nació en año bisiesto.")
    else:
        print("Ningún integrante nació en año bisiesto.")


# --- Prueba rápida de la función ---
if __name__ == "__main__":
    anios = [1992, 1994, 1987, 1999, 2002]
    verificar_bisiestos(anios)
