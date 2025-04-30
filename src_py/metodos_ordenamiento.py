##creen una clase MetodosOrdenamiento
#Crear un metodo sort bubble que reciba un arreglo el metodo solo imprima un mensaje

class MetodosOrdenamiento:      
    def sort_bubble(self,array):
        arreglo=array.copy()
        n=len(arreglo)
        for i in range(n):
            for j in range(i+1,n):
                if arreglo[i]>arreglo[j]:
                    arreglo[i], arreglo[i]=arreglo[j], arreglo[j]

    def sort_bubble_mejorado(self,array):
        arreglo=array.copy()
        n=len(arreglo)
        for i in range(n):
            for j in range(i+1,n):
                if arreglo[i]>arreglo[j]:
                    arreglo[i], arreglo[j]=arreglo[j], arreglo[i]
        return arreglo
    def sort_selection(self,array):
        arreglo=array.copy()
        n=len(arreglo)
        for i in range(n):
            min_index=i
            for j in range(i+1,n):
                if arreglo[j]<arreglo[min_index]:
                    min_index=j
            arreglo[i], arreglo[min_index]=arreglo[min_index], arreglo[i]
        return arreglo