class TestRun():

    def check_operation(self, metodo, lista, largo_lista):

        lista_original = list(lista)
        lista_ordenada = sorted(lista)
        lista_metodo = metodo(lista, largo_lista)
        funcionamiento = (lista_metodo == lista_ordenada)

        resultados = {
            "Lista Original" : lista_original,
            "Lista Ordenada" : lista_ordenada,
            "Lista Procesada" : lista_metodo,
            "Funcionamiento" : funcionamiento
        }

        return resultados
