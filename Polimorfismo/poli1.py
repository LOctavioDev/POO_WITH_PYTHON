#BASICAMENTE ES HACER ES QUE CUANDO LE DEMOS UN METODO A UN OBJETO SE COMPORTE DIFERENTE ENTENDIENDO QUE SUS PROPIEDADES SON DIFERENTES
class Gato():
    def sonido(self):
        return "Miau"

class Perro():
    def sonido(self):
        return "Guau"
    
def hacer_sonido(animal):
    print(animal.sonido())
    
    
gato = Gato()
perro = Perro()

print(perro.sonido())

print(hacer_sonido(gato))  #ESTAMOS LLAMANDO A gato Y SE APLICA EL POLIMORFISMO
#EL MIMSO METODO FUNCIONA DIFERENTE PARA DIFERNETES OBJETOS