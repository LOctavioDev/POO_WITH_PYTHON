#Permite que una clase adquiera atributos y métodos de otra clase, estableciendo una jerarquía de relaciones. Una clase derivada hereda características de la clase base, lo que fomenta la reutilización y extensión del código.

class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    def hablar(self):
        print('Hola estoy hablando un poco')
        
class Empleado(Persona): #HACEMOS QUE LA CLASE EMPLEADO HEREDE LOS ATRIBUTOS DE LA CLASE PERSONA
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario): 
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario
    def hablar(self):
        print('NO')
        
class Estudiante(Persona): 
    def __init__(self, nombre, edad, nacionalidad, notas, universidad): 
        super().__init__(nombre, edad, nacionalidad)
        self.notas = notas
        self.universidad = universidad
        
    def hablar(self):
        print('NO')
        
roberto = Empleado('Roberto', 25, 'asutriaco', "Peluqero", 13000) #SON LAS MISMAS PROPIEDADES QUE LAS DE LA CLASE PERSONA
roberto.hablar()

#A TODO ESTO SE LE DICE HERENCIA SIMPLE, 