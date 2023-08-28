#EN CORTAS PALABRAS LA ABSTRACCION ES LA IDEA DE OCULTAR LOS DETALLES COMPLEJOS DE IMPLEMNETACION Y MOSTRAR SOLO LOS ASPECTOS RELEVANTES
class Auto():
    def __init__(self):
        self._estado = "apagado"
    
    def encender(self):
        self._estado = "encendido"
        print("El auto esta encendido")
    
    def conducir(self):
        if self._estado == "apagado":
            self.encender()
        print("Conduciendo el auto")
        
auto = Auto()
auto.conducir() #ACA YA HAY ABSTRACCION PORQUE... EL USUARIO NO SABE QUE PRIMERO ESTOY REVISANOD SI YA ESTA ENCENDIDO 