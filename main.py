from clases.insercion_dicotomica import dicotomia1, dicotomia2


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
   print("Ordenando a partir de una lista vacia, la lista es : {}".format(resultado2.orde))



   from clases.ordenacion_topológica import *