#LOS METODOS MAGICOS O METODOS DUNDER... SON FUNCIONES QUE TIENEN UN NOMBRE ESPECIAL ASIGNADO INICIAN Y TERMINAN CON DOS GUIONES BAJOS "__p__"
class Persona:
    def __init__(self, nombre, edad):   #__init__ ES UN EJEMPLO CLARO DE LO QUE ES UN METODO ESPECIAL YA QUE CONSTRUYE EL OBJETO
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self):#str LO QUE HACE ES DEVOLVER UNA REPRESENTACION DEL OBJETO EN UNA CADENA DE TEXTO
        return f'Persona(nombre = {self.nombre},edad = {self.edad})'
    
    def __repr__(self):
        return
    
    
octavio = Persona('Octavio', 19)


print(octavio)  #ACA DEVUELVE UNA REPRESENTACION PARA HUMANOS

lista = (1,2,3)

print(lista)    #LA RAZON POR LA CUAL TE MUESTRA LA "lista" ES PORQUE LAS LISTAS SON OBJETOS... (BUENO POR QUE TODO ES UN OBJETO EN PYTHON) Y LO QUE SE HACA ES MUY SIMILAR AL METODO MAGICO DE __str__