#CREAR UNA CLASE ESTUDIANTE QUE TENGA COMO ATRIBUTOS EL NOMBRE, LA EDAD Y EL GRADO. QUE TENGA CMO METODOS estudiar() QUE IMPIRMA EL MENSAJE: "EL estudiante (nombre) esta estudiando"

class Estudiante():
    def __init__ (self,nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    def estudiar(self):
        print('Estudiando....')

nombre = input('INGRESE SU NOMBRE: ')
edad = int(input('INGRESE SU EDAD: '))
grado = int(input('INGRESE SU GRADO: '))

estudiante = Estudiante(nombre,edad,grado)

print(f'''
       El estudiante se llama {estudiante.nombre} de edad {estudiante.edad} cursa el {estudiante.grado} grado   
    ''')

while True:
    estudiar = input()
    if estudiar.lower() == "estudiar" :
        estudiante.estudiar()