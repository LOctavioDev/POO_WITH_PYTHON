#EN POCAS PALABRAS EL SINGLE RESPONSIBILITY PRINCIPLE... QUIERE DECIR QUE UNA CLASE DEBE TENER UNA Y SOLO UNA RAZON PARA CAMBIAR

class TanqueDeCombustible:
    def __init__(self):
        self.combustible = 100  #EL TANQUE COMBUSTIBLE TENE UNA PROPIEDAD ESTATICA 
    
    def agregar_combustible(self, cantidad):
        self.combustible += cantidad
    
    def obtener_combustible(self):
        return self.combustible   
    
    def usar_combustible(self,cantidad):
        self.combustible -= cantidad


class Auto():
    def __init__(self, tanque):
        self.posicion = 0
        self.tanque = tanque
        
    def mover(self, distancia):
        if self.tanque.obtener_combustible() >= distancia / 2:
            self.posicion += distancia
            self.tanque.usar_combustible(distancia / 2)
            print("HAS MOVIDO EL AUTO EXITOSAMENTE")
        else:
            print('NO HAY SUFICIENTE COMBUSTIBLE')
    
    def obtener_posicion(self,):
        return self.posicion
    
    # def agregar_combustible(self, cantidad):
    #     self.combustible += cantidad
        
    # def obtener_combustible(self):
    #      return self.combustible
     
     
    #EL CODIGO ANTERIOR TIENE UN PROBLEMA, YA QUE NO RESPETA EL PRICIPIO DE RESPONSABILIDAD UNICA... NO ES EFICIENTE QUE LA CLASE AUTO MUEVA AL AUTOMOVIL Y QUE TAMBIEN AGREGUE EL COMBUSTIBLE 


#ESTO ES LO CORRECTO:

        
tanque = TanqueDeCombustible()
carro = Auto(tanque)

print(carro.obtener_posicion())
print(carro.mover(10))
print(carro.obtener_posicion())
print(carro.mover(20))
print(carro.obtener_posicion())
print(carro.mover(50))
print(carro.obtener_posicion())
print(carro.mover(200))
print(carro.obtener_posicion())