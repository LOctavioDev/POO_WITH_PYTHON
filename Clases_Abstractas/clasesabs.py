#UNA CLASE ABSTRACTA ES UNA CLASE QUE NO PODEMOS INSTANCIAR POR SI SOLA... ES UNA ESPECIA DE PLANTILLA PARA PODER CREAR CLASES A PARTIR DE ELLA
from abc import ABC, abstractclassmethod    #abc ES UNA CLASE AUXILIAR... EN PYTHON UNA METACLASE ES UNA CLASE DE LA CLASE POR ASI DECIRLO

class Persona(ABC):
    @abstractclassmethod
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad
    
    @abstractclassmethod
    def hacer_actividad(self):
        pass
    
    def presentarse(self):
        print(f'Hola, me llamo: {self.nombre} y tengo {self.edad} anios')
        

class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)
    
    def hacer_actividad(self):
        print(f'Estoy estudiando: {self.actividad}')
        

class Trabajador(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)
    
    def hacer_actividad(self):
        print(f'Actualmente estoy trabajando en el rubro de: {self.actividad}')


octavio = Estudiante("Octavio", 19, "masculino", "programacion")

yayo = Trabajador("Haziel", 18, "no binario", "programacion")

octavio.presentarse()
octavio.hacer_actividad()

yayo.presentarse()
yayo.hacer_actividad()
