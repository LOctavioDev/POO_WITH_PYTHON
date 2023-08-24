class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        
    def hablar(self):
        print('Hola estoy hablando un poco')
        
        
class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad
    
    def mostrar_habilidad(self):
        print(f'Mi habilidad es: {self.habilidad}')
        
        
class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.salario = salario
        self.empresa = empresa
    
    def presentarse(self):
        return f'{super().mostrar_habilidad()}'
        
        
octavio = EmpleadoArtista('Octavio', 19, 'mexicana', 'fumar', 96000, 'Apple')
octavio.presentarse()


herencia = issubclass(Artista, Persona)
instanica = isinstance(octavio, EmpleadoArtista)

print(f'HERENCIA: {herencia}    ...     INSTANCIA: {instanica}')