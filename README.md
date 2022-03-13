# EJERCICIOS DE ORDENAR

# Main

if __name__ == "__main__":

   from clases.insercion_dicotomica import *
   print("El ejercicio 1:")
   print("Primer apartado: ")
   tabla = [3,6,2,9,4,8,1,5,7,0]
   print(tabla)
   resultado= dicotomia1(tabla)
   print("La tabla ordenada por dicotomia es: {}".format(resultado.ordenar()))

   print("Segundo apartado: ")
   resultado2= dicotomia2(tabla)
   print("Ordenando a partir de una lista vacia, la lista es : {}".format(resultado2.ordenar_vacia()))



   from clases.ordenacion_topológica import *
   print("El ejercicio 2: ")
   vector = [3, -8, 9, 6, 19, -4, 1, 9, 8, -1]
   resultado = lista(vector)
   print("El resultado de este ejercicio tras ordenarse: {}".format(resultado.ordenacion_burbuja()))


   from clases.esta_explorado import *
   print("El ejercicio 3: ")
   vector = [3, -8, 9, 6, 19, -4, 1, 9, 8, -1]
   resultado = segmento_de_tablas(vector)
   print("Los segmentos de {} son: {}".format(vector, resultado.segmento_de_tablas()))
   print("Tras aplicar la funcion explorar los segmentoss quedan de la siguiente manera: ")
   print(resultado.esta_explorado(resultado.segmento_de_tablas()[0]), " - ", resultado.esta_explorado(resultado.segmento_de_tablas()[1]))



# Ejercicio 1: Insercion Dicotomica

"Primera Parte"
class dicotomia1:
    def __init__(self, tabla):
        self.tabla = tabla

    def ordenar(self):
        self.tabla.sort()
        return self.tabla
        
"Segunda Parte"
class dicotomia2:
    def __init__(self, tabla):
        dicotomia1.__init__(self, tabla)
        r=[]
        self.r =r
    
    def ordenar_vacia(self):
        dicotomia1.ordenar(self)
        for i in self.tabla:
            self.r.append(i)
        return self.r



# Ejercicio 2: Ordenación topológica

class lista:
    def __init__(self,lista):
        self.lista=lista

    def ordenacion_burbuja(self):
      for i in range(len(self.lista)-1):
        for j in range(len(self.lista)-1):
          if self.lista[j] > self.lista[j+1]:
            print("Intercambiamos {} con {}".format(self.lista[j], self.lista[j+1]))
            self.lista[j], self.lista[j+1] = self.lista[j+1], self.lista[j]
      return self.lista



# Ejercicio 3: Esta explorado

class segmento_de_tablas:

    def __init__(self,tabla):
        self.tabla = tabla

    def segmentos(self):
        r=[]
        for i in range(len(self.tabla)-1):

            if self.tabla[i] >= self.tabla[i+1]:
                r.append(self.tabla[i+1])

                if self.tabla[i+1] < self.tabla[i+2]:
                    r.append(self.tabla[i+1])
                    n=[]
                    for j in range(i+2, len(self.tabla)-1):
                        if self.tabla[j] >= self.tabla[j+1]:
                            n.append(self.tabla[j])
                            if self.tabla[j+1] < self.tabla[j+2]:
                                n.append(self.tabla[j+1])
                                return r, n
            else:
                pass


    def explorar(self, segmento_de_tablas):
        mi = segmento_de_tablas[0]
        segmento_de_tablas = segmento_de_tablas[1:] + segmento_de_tablas[:1]
        return segmento_de_tablas





