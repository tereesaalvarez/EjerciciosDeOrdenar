class segmento_de_tablas:

    def __init__(self,tabla):
        self.tabla = tabla

    def segmentos(self):
        r=[]
        for i in range(len(self.tabla)-1):
            for j in range(len(self.lista)-1):
            if self.lista[j] > self.lista[j+1]:
           
            print("Intercambiamos {} con {}".format(self.lista[j], self.lista[j+1]))
            self.lista[j], self.lista[j+1] = self.lista[j+1], self.lista[j]
      return self.lista