#EL INTERFACE SEGREGATION PRINCIPLE... BASICAMENTE DICE QUE NINGUN CLIENTE TIENE QUE SER FROZADO A DEPENDER DE INTERFACES QUE NO UTILICE 
from abc import ABC, abstractclassmethod

# class Trabajador(ABC):
    
#     @abstractclassmethod
#     def comer(self):
#         pass
    
#     @abstractclassmethod
#     def trabajar(self):
#         pass
    
#     @abstractclassmethod
#     def dormir(self):
#         pass

    
# class Humando(Trabajador):
#     def comer(self):
#         print('EL HUMANDO ESTA COMIENDO')
    
#     def trabajar(self):
#         print('EL HUMANDO ESTA TRABAJANDO')

#     def dormir(self):
#         print('EL HUMANDO ESTA DURMIENDO')


# class Robot(Trabajador):
#     def trabajar(self):
#         print('EL ROBOT ESTA TRABAJANDO')

# robot = Robot()     


# #EN ESTE CASO NO NOS DEJARA CREAR UN ROBOT POR QUE TIENE QUE TENER LOS METODOS DE LA CLASE TRABAJADOR, O SEA ESTAMOS OBLIGADOS A USAR METODOS QUE NO VAMOS A OCUPAR


#ASI SERIA LO CORRECTO:


class Trabajador(ABC):
    
    @abstractclassmethod
    def trabajar(self):
        pass


class Comedor(ABC):
    @abstractclassmethod
    def comer(self):
        pass
    
    
class Durmiente(ABC):
    @abstractclassmethod
    def dormir(self):
        pass

    
class Humano(Trabajador, Durmiente, Comedor):
    def comer(self):
        print('EL HUMANDO ESTA COMIENDO')
    
    def trabajar(self):
        print('EL HUMANDO ESTA TRABAJANDO')

    def dormir(self):
        print('EL HUMANDO ESTA DURMIENDO')


class Robot(Trabajador):
    def trabajar(self):
        print('EL ROBOT ESTA TRABAJANDO')

robot = Robot() 
humano = Humano()

robot.trabajar()
humano.comer()