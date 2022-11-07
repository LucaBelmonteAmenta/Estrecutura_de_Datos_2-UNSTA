from Metodos import Burbuja, Insercion, Seleccion, Shell, MergeSort, QuickSort
from ProfilerReportGenerator import ProfilerReportGenerator
from TestRun import TestRun 

Listas = [
    [12, 99, 35, 51, 4, 16, 89, 1, 15, 25],
    [1, 10, 22, 33, 56, 68, 87, 98],
    [43, 36, 32, 27, 20, 19, 15, 8, 1],
    [74, 14, 21, 44, 38, 97, 11, 78, 65, 88, 30]
    ]


Metodos = {
    "Burbuja - 1" : Burbuja.Metodo1,
    "Burbuja - 2" : Burbuja.Metodo2,
    "Burbuja - 3" : Burbuja.Metodo3, 
    "Inserción Directa" : Insercion.Metodo1,
    "Inserción Binaria" : Insercion.Metodo2,
    "Seleccion - 1" : Seleccion.Metodo1,
    "Seleccion - 2" : Seleccion.Metodo2,
    "Shell" : Shell.Metodo,
    "Merge Sort" : MergeSort.Metodo,
    "Quick Sort" : QuickSort.Metodo
    }


if __name__=="__main__":

    lista = Listas[3]
    largo_lista = len(lista) - 1
    nombre_metodo = "Quick Sort"
    metodo = Metodos[nombre_metodo]

    prueba_funcionamiento = TestRun()
    generador_reporte = ProfilerReportGenerator()

    resultado = prueba_funcionamiento.check_operation(metodo ,list(lista), largo_lista)
    generador_reporte.Generate_Profiler_Report(nombre_metodo, metodo, list(lista), largo_lista)

    print(f"La lista antes del metodo:  " + str(resultado["Lista Original"]))
    print(f"Autentica lista ordenada:   " + str(resultado["Lista Ordenada"]))
    print(f"Lista pasado por el metodo: " + str(resultado["Lista Procesada"]))
    print(f"Funcionamiento del metodo:  " + str(resultado["Funcionamiento"]))

    
    
