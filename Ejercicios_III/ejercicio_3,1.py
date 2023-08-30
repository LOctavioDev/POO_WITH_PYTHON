#CREAR UN JUEGO DE FUSION... EL JUEGO CONSISTE EN CREAR PERSONAJES UN JUEGO Y QUE ESOS PERSONAJES SE PUEDAN FUSIONAR PARA FORMAR PERSONAJES MAS PODEROSOS QUE TENGAN MAS PODER ...
#PARA ELLO DEBREMOS CAMBIAR EL COMPORTAMENTO DEL OPERADOR "+" PARA QUE CUANDO LOS PERSONAJES SE FUSIONEN, SALGA UN NUEVO PERSONAJE CON HABILIDADES MEJORADAS 

class Personaje:
    def __init__(self, nombre, fuerza, velocidad):
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad
    
    def __repr__(self):
        return f"{self.nombre} (Fuerza: {self.fuerza}), (Velocidad: {self.velocidad})"
    
    def __add__(self, otro_pj):
        nuevo_nombre = self.nombre + "-" + otro_pj.nombre
        nueva_fuerza = round(((self.fuerza + otro_pj.fuerza) / 2) ** 1.3)
        nueva_velocidad = round(((self.velocidad + otro_pj.velocidad) / 2) ** 1.3)
        return Personaje(nuevo_nombre, nueva_fuerza, nueva_velocidad)
    
    
goku = Personaje('Goku', 100, 120)
vegeta = Personaje('Vegeta', 110, 98)
freezer = Personaje('Freezer', 200, 190)

gogeta = goku + vegeta
freeku = freezer + goku
freegeta = freezer + gogeta

print(gogeta)
print(freeku)
print(freegeta)