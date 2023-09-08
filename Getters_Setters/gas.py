#SON DOS METODOS QUE SE UTILIZAN PARA ACCEDER Y MODIFICAR A LAS PROPIEDADES PRIVADAS QUE TIENEN LAS CLASES
class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre   #CUANDO HAY UN GUION BAJO QUEIRE DECIR QUE NO DEBE ACCEDER DE ESTA FORMA DE ARIBUTO, HACERLO DE OTRA FORMA
        self._edad = edad
        
    def get_nombre(self):       #GETTER
        return self._nombre
    
    def set_nombre(self, new_nombre):   #SETTER
        self.nombre = new_nombre

octavio = Persona('Octavio', 19)

print(octavio.get_nombre())
