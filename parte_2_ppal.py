# === Importación de funciones ===

# Imports parte A
from A_ingreso_dnis import ingresar_dnis
from A_conjuntos_digitos import crear_conjuntos_digitos
from A_operaciones_conjuntos import operaciones_conjuntos
from A_analisis_dnis import analizar_dnis
from A_evaluacion_logica import evaluar_logica

# Imports parte B
from B_ingreso_anios import ingresar_anios
from B_contador_pares_impares import contar_pares_impares
from B_verificacion_z import verificar_grupo_z
from B_anio_bisiesto import verificar_bisiestos
from B_calculo_edades import calcular_edades
from B_productos_cartesianos import producto_cartesiano
from datetime import date


# === Función principal ===

def main(modo):
    print("=== PROGRAMA PRINCIPAL - TRABAJO PRÁCTICO ===")
    
    if modo.lower() == "a":
        # Parte A: Operaciones con DNIs
        print("\n--- PARTE A: OPERACIONES CON DNIs ---")
        
        # 1. Ingreso de DNIs
        print("\n1. Ingreso de DNIs:")
        dnis = ingresar_dnis()
        
        # 2. Análisis individual de DNIs
        print("\n2. Análisis individual de DNIs:")
        analizar_dnis(dnis)
        
        # 3. Operaciones con conjuntos
        print("\n3. Operaciones con conjuntos de dígitos:")
        conjuntos_digitos = crear_conjuntos_digitos(dnis)
        operaciones_conjuntos(conjuntos_digitos)
        
        # 4. Evaluación lógica
        print("\n4. Evaluación de condiciones lógicas:")
        evaluar_logica(conjuntos_digitos)
    
    elif modo.lower() == "b":
        # Parte B: Operaciones con años de nacimiento
        print("\n--- PARTE B: OPERACIONES CON AÑOS DE NACIMIENTO ---")
        
        # 1. Ingreso de años
        print("\n1. Ingreso de años de nacimiento:")
        anios = ingresar_anios()
        
        # 2. Conteo de pares/impares
        print("\n2. Conteo de años pares e impares:")
        contar_pares_impares(anios)
        
        # 3. Verificación Grupo Z
        print("\n3. Verificación de Grupo Z:")
        verificar_grupo_z(anios)
        
        # 4. Verificación años bisiestos
        print("\n4. Verificación de años bisiestos:")
        verificar_bisiestos(anios)
        
        # 5. Producto cartesiano
        print("\n5. Producto cartesiano (años × edades):")
        edades = calcular_edades(anios)
        producto_cartesiano(anios, edades)
    
    else:
        print("Modo inválido. Usar 'a' o 'b'.")
    
    print("\n=== PROGRAMA FINALIZADO ===")


# Control de la ejecución
if __name__ == "__main__":
    main("b")
