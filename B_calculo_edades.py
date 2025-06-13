from datetime import date   # Importamos el módulo para obtener el año actual 

def calcular_edades(anios):
    """
    Calcula la edad actual para cada año de nacimiento ingresado.
    Devuelve una lista de edades.
    """
    anio_actual = date.today().year # Obtenemos el año actual desde el sistema 
    return [anio_actual - anio for anio in anios]   # Calculamos cada edad 


# --- Prueba rápida de la función ---
if __name__ == "__main__":
    anios = [1990, 1995, 2000, 2005, 2010]
    edades = calcular_edades(anios)
    print("Años de nacimiento:", anios)
    print("Edades actuales:", edades)