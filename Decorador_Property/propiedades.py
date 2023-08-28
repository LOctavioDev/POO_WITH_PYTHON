class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self._edad = edad
    
    @property   #SE PUEDE DECIR QUE ES UN DECORADOR ESPECIAL... DICE QUE TODO ESTE BLOQUE DE CODIGO ES UN GETTER
    def nombre(self):
        return self.__nombre 
    
    @nombre.setter   
    def nombre(self, new_nombre):
        self.__nombre = new_nombre
    
    @nombre.deleter   
    def nombre(self):
        del self.__nombre           


octavio = Persona('Octavio', 19)
nombre = octavio.nombre #SI SE FIJAN EN LA LINEA 3... ESTAMOS OCULTANDO EL NOMBRE REAL DE LA VARIABLE
print(nombre)


octavio.nombre = "DALTO"

nombre = octavio.nombre
print(nombre)


del octavio.nombre 

nombre = octavio.nombre
print(nombre)