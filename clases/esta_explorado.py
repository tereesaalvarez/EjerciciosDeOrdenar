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