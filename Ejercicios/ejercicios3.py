class Animal:
    def comer(self):
        print('EL ANIMAL ESTA COMIENDO')

class Ave(Animal):
    def volar(self):
        print('EL ANIMAL ESTA VOLANDO')

class Mamifero(Animal):
    def amamantar(self):
        print('EL ANIMAL ESTA AMAMANTANDO')
        
class Murcielago(Mamifero, Ave):
    pass

murcielago = Murcielago()
murcielago.comer()
murcielago.amamantar()
murcielago.volar()