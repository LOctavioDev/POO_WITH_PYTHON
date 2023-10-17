#EL MRO (METHOD RESOLUTION ORDER) HACE REFERENCIA AL ORDEN EN EL QUE PYTHON BUSCA METODOS Y ATRIBUTOS EN LAS CLASES
class A:
    def hablar(self):
        print("HABLAR DESDE: A")
        
class B(A):
    def hablar(self):
        print("HABLAR DESDE: B")
        
class C(A):
    def hablar(self):
        print("HABLAR DESDE: C")
        
class D(B,C):
    pass
        
d = D()

C.hablar(d)
