#EL encapsulamiento se refiere a la práctica de ocultar los detalles internos y la implementación de una clase a otras partes del programa.
class MiClase:
    def __init__(self):
        self.__atributo_privado = "Valor" #ESTO VA A SER UN DATO ENCAPSULADO
    
    def __hablar(): #METODOS PRIVADOS
        print("Hola, que tal")
        

objeto = MiClase()

print(objeto._atributo_privado)
print(objeto.__hablar())