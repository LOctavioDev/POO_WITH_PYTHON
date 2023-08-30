#LA SOBRECARGA DE OPERACIONES ES LA CAPACIDAD DE UNA CLASE PARA DEFIFINIR EL COMPORTAMIENTO DE OPERADORRES COMUNES COMO: (+,-,*,/) Y MAS
class Persona: 
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def __str__(self):
        return f'Persona(nombre = {self.nombre}, edad = {self.edad})'
    
    def __repr__(self):
        return f'Persona("{self.nombre}", {self.edad})'
    
    def __add__(self, otro): #OTRO HACE REFERENCIA A LO QUE QUEREMOS SUMAR
        nuevo_valor = self.edad + otro.edad
        return Persona(self.nombre + otro.nombre, nuevo_valor)
        
        
jesus = Persona('Jesus', 23)
haziel = Persona('Haziel', 18)
briones = Persona('Briones', 19)

nueva_persona = jesus + haziel + briones #ACABO DE DEFINIR QUE PASA CON LOS OBJETOS CUANDO LOS SUMO

print(nueva_persona.nombre)
print(nueva_persona.edad)   #ACA ACABAMOS DE DEFINIR COMO SE VA A COMPORTAR LOS OBJETOS DE LA CLASE PERSONA CUANDO LOS SUMAMOS