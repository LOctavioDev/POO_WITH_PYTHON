#CREAR UN SISTEMA PARA UNA ESCUELA. EN ESTE SIETMA VAMOS A TENER DOS CLASES PRINCIPALES: Persona y Estudiante. LA CLASE PERSONA TENDRA LOS ATRIBUTOS DE NOMBRE Y EDAD Y UN METODO QUE IMPIRMA EL NOMBRE Y LA EDAD DE LA PERSONA. LA CLASE ESTUDIANTE HEREDAAR DE LA CLASE PERSONA Y TAMBIEN TENDRA UN ATRIBUTO ADICIONAL: Grado Y UN METODO QUE IMPRIMA EL GRADO DEL ESTUDIANTE.

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def mostrar_datos(self):
        print(f'EL NOMBRE DE LA PERSONA ES: {self.nombre} Y TIENE {self.edad} DE EDAD')        

class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado
    
    def mostrar_grado(self):
        print(f'GRADO {self.grado}') 
        
estudiante = Estudiante('Juan', 19, 4)
estudiante.mostrar_datos()
estudiante.mostrar_grado()