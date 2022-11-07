from asyncio.windows_events import NULL
from unicodedata import name
from line_profiler import LineProfiler
from io import StringIO


class ProfilerReportGenerator():

    # Se obtiene la dirección o ruta en la que se encuentra el .py en el que está esta clase
    def direccion_modulo(self):
        
        ruta = __file__
        lista = ruta.split('\\')
        lista = lista[0:-1]

        return '\\'.join(lista)

    # Se crea un archivo .txt y se guarda allí lo que se hubiera impreso por consola deotra forma
    def Record_Print(self, nombre_funcion, recolector_datos):
        
        output = recolector_datos.getvalue()
        output = output.rstrip()
        
        nombre_nuevo_archivo = "\Informe Profiler (" + nombre_funcion + ").txt"
        direccion_nuevo_archivo = self.direccion_modulo() + nombre_nuevo_archivo

        file = open(direccion_nuevo_archivo, 'w')
        file.write(output)
        file.close()

        return direccion_nuevo_archivo
        
    # Se generá un informe que describe al analisis de ejecución de la función pasada como parametro
    def Generate_Profiler_Report(self, nombre_funcion, funcion, Parametro1, Parametro2, funcion_auxiliar = NULL):
        
        recolector_datos = StringIO()
        
        Analizador = LineProfiler()

        if funcion_auxiliar is not NULL:
            Analizador.add_function(funcion_auxiliar)

        analisis = Analizador(funcion)
        analisis(Parametro1, Parametro2)

        Analizador.enable_by_count()
        Analizador.print_stats(recolector_datos)

        self.Record_Print(nombre_funcion, recolector_datos)


if __name__ == "__main__":

    generador_reporte = ProfilerReportGenerator()
    generador_reporte.Generate_Profiler_Report(0,0,0)
    




    
