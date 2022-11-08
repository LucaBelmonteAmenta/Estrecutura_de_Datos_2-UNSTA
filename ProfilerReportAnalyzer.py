import re
remove_all = lambda lista, valor_remover : list([value for value in lista if value != valor_remover])


class Codigo():

    tipos_comparadores = [
        " == ", " != ", " <= ", " >= ", " < ", " > ", 
        " and ", " not ", " or ", " & ", " | " 
    ]

    tipos_operaciones_elementales = [
        "+", "-", "/", "*", 
        " = ", "[", 
        "range(", "not", "return"
    ] + tipos_comparadores

    def __init__(self, numero_linea = 0, linea_codigo = "", numero_ejecuciones = 0):
        self.numero_linea = numero_linea
        self.linea_codigo = linea_codigo
        self.numero_ejecuciones = numero_ejecuciones

    def operaciones_elementales(self):
        
        cantidad_operaciones_elementales = 0
        for operacion_elemental in self.tipos_operaciones_elementales:
            cantidad_operaciones_elementales += self.linea_codigo.count(operacion_elemental)

        return cantidad_operaciones_elementales    
    
    def operaciones_elementales_totales(self):
        return (self.operaciones_elementales() * int(self.numero_ejecuciones))

    def hay_movimiento_lista(self):
        condicion_1 = ((self.linea_codigo.find("lista[")) == 0)
        condicion_2 = ((self.linea_codigo.find("lista[")) < self.linea_codigo.find(" = "))
        return condicion_1 and condicion_2 

    def cantidad_comparaciones_elementos_lista(self):
        
        codigo_dividido = re.split(r'[)(]', self.linea_codigo)
        contador_comparadores = 0
        for componente in codigo_dividido:
            for comparador in self.tipos_comparadores:
                condicion_1 = comparador in componente
                condicion_2 = "lista[" in componente
                if condicion_1 and condicion_2:
                    contador_comparadores += 1
                    break
            
        return contador_comparadores

    def cantidad_comparaciones_elementos_lista_totales(self):
        return self.cantidad_comparaciones_elementos_lista() * int(self.numero_ejecuciones)

    def imprimir(self):
        print("Numero de linea: ", self.numero_linea)
        print("Codigo de la linea: ", self.linea_codigo)
        print("Numero de ejecuciones: ", self.numero_ejecuciones)
        print("Operaciones elementales: ", self.operaciones_elementales())
        print("Operaciones elementales totales: ", self.operaciones_elementales_totales())
        print("Hay movimiento de un elemento de la lista: ", self.hay_movimiento_lista())
        print("Cantidad de comparaciones entre los elementos de la lista: ", self.cantidad_comparaciones_elementos_lista())
        print("--------------------------------------------------------------------------------")


class ProfilerReportAnalyzer(): 

    def ExtractCodeLines(self, lineas_archivo):    
        
        lineas_codigo = []
        bandera_aparicion_codigo = False
            
        for line in lineas_archivo:
            
            renglon =  line.split(" ")
            separador = "=========="
            
            if renglon:

                renglon = remove_all(renglon, "")

                
                if separador in renglon[0]:
                    bandera_aparicion_codigo = True

                if (bandera_aparicion_codigo) and (len(renglon)>1):
                    
                    numero_linea = renglon[0]

                    if (renglon[1].isnumeric()):
                        numero_ejecuciones = renglon[1]
                        linea_codigo = " ".join(renglon[5:len(renglon):1])
                    else:
                        numero_ejecuciones = 0
                        linea_codigo = " ".join(renglon[1:len(renglon):1])

                    linea_codigo = linea_codigo[0:-1]

                    codigo = Codigo(numero_linea, linea_codigo, numero_ejecuciones)
                    
                    #codigo.imprimir()

                    lineas_codigo.append(codigo)
        
        return lineas_codigo

    def ExtractRuntime(self, lineas_archivo): 
        
        tiempo_ejecucion = ""
        
        for line in lineas_archivo:
            if ("Total time" in line):
                renglon =  line.split(": ")
                tiempo_ejecucion = renglon[1][0:-1]
                break

        return tiempo_ejecucion




    def GenerateReportAnalysis(self, nombre_archivo_informe):

        archivo = open(nombre_archivo_informe , mode="r")
        
        if (archivo.readable()):
            lineas_archivo = archivo.readlines()
            tiempo_ejecucion = self.ExtractRuntime(lineas_archivo)
            codigo_funcion = self.ExtractCodeLines(lineas_archivo)
            
        archivo.close()

        cantidad_operaciones_elementales = 0
        cantidad_movimientos_lista = 0
        cantidad_comparaciones_elementos = 0

        for linea in codigo_funcion:
            cantidad_operaciones_elementales += linea.operaciones_elementales_totales()
            cantidad_comparaciones_elementos += linea.cantidad_comparaciones_elementos_lista_totales()
            if linea.hay_movimiento_lista():
                cantidad_movimientos_lista += int(linea.numero_ejecuciones)     

        data_report = {
            "Tiempo total de la ejecución" : tiempo_ejecucion, 
            "Cantidad de operaciones elementales" : cantidad_operaciones_elementales,
            "Cantidad de movimientos de elementos" : cantidad_movimientos_lista,
            "Cantidad de comparaciónes entre elementos" : cantidad_comparaciones_elementos
        }

        return data_report




if (__name__ == "__main__"):
    
    ruta_informe = "C:/GitHub/Estrecutura_de_Datos_2-UNSTA/Informe Profiler (Inserción Directa).txt"
    analizador_reporte = ProfilerReportAnalyzer()
    analisis_reporte = analizador_reporte.GenerateReportAnalysis(ruta_informe)
    print(analisis_reporte)

    linea = " if (auxiliar_1 < lista[k]) & (auxiliar_2 < lista[k]) & (x < 0):"
    codigo_prueba = Codigo(0, linea, 1)
    print(codigo_prueba.cantidad_comparaciones_elementos_lista())
    print(codigo_prueba.operaciones_elementales_totales())









