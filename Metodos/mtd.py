# SIMPLEMENTE, UN METODO ES UNA FUNCION
class Celular:
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
    
    def llamar(self): #ES LO MISMO QUE UNA FUNCION SOLO QUE CUANDO ESTA DENTRO DE LA CLASE SE LE DICE METODO
        print(f'Estas haciendo un llamado desde un: {self.modelo}')

    def cortar(self):   #DEBE SE ESATR SELF PARA PODER HACER REFERENCIA AL OBJETO
        print('Cortaste la llamada')


celular1 = Celular("Samsung","S23","48MP")
celular2 = Celular("Apple","Iphone 14 pro","48MP")

celular1.llamar()