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