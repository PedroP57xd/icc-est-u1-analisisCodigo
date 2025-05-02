from benchmarking import Benchmarking 
from metodos_ordenamiento import MetodosOrdenamiento
if __name__ == "__main__":  
    print("Funciona"); 
    bench=Benchmarking()
    metodosO= MetodosOrdenamiento()

    # tam=1000
    tam=[5000, 10000, 15000, 20000]
    
    arreglo_base = bench.build_arreglo(tam)
    

    medodos_dic ={
        "Burbuja": metodosO.sort_bubble,
        "Burbuja Mejorado": metodosO.sort_bubble_mejorado,
        "Seleccion": metodosO.sort_selection,
        "Shell": metodosO.sort_shell,
    }

    resultados = []
    
    for tam in tam:
        arreglo_base = bench.build_arreglo(tam)
        for nombre, metodo in medodos_dic.items():
            tiempo_resultado= bench.medir_tiempo(metodo, arreglo_base)
            tupla_resultado = (tam, nombre, tiempo_resultado)
            resultados.append(tupla_resultado)
    for tam,nombre,tiempo in resultados:
            print(f"tamaño: {tam}, Nombre metodo: {nombre}, tiempo: {tiempo:6f}")