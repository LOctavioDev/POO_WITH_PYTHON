#LOS ATRIBUTOS SON VARIABLES QUE PERTENECEN A UNA CLASE
class Celular():
    def __init__(self, marca, modelo, camara):  #EL self ES UNA FROMA DE HACER REFERENCIA A SI MISMO
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
        
celular1 = Celular("Samsung", "S22", "48MP")    #CREAMOS EL OBJETO

print(celular1.camara)  #ACCEDEMOS A SUS ATRIBUTOS