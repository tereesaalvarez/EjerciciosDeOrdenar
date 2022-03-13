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
        self=r
    
    def ordenar(self):
        dicotomia1.ordenar(self)
        for i in self.tabla:
            self.append(i)
        return self