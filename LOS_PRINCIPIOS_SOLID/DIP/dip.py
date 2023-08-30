#EL DEPENDENDENCY INVERSION PRINCIPLE... ESTO DICE QUE LOS MODULOS DE ALTO NIVEL NO DEBEN DE DEPENDER DE LOS DE BAJO NIVEL SI NO QUE DEBEN DE DEPENDER DE LAS ABSTRACCIONES... Y LO SEGUNDO ES QUE LAS ABSTRACCIONES NO DEBEN DE DEPENDER DE LOS DETALLES SI NO QUE LOS DETALLES DEBEN DE DEPENDER DE LAS ABSTRACIONES
#IMAGINEMOS QUE VAMOS A CREAR UN PROGRAMA DE PROCESAMIENTO DE TEXTO 


# class Diccionario:
#     def verificar_palabra(self, palabra):
#         #LOGICA PARA VERIFICAR LA PALABRA
#         pass
    

# class CorrectorOrtografico:
#     def __init__(self):
#         self.diccionario = Diccionario()
        
#     def corregir_texto(self, texto):
#         #USAMOS EL DICCIONARIO PARA CORREGIR EL TEXTO
#         pass


#ACA SE ESTA ROMPIEDO EL PRINCIPIO DEBIDO A QUE LA CLASE CORRECTORORTOGRAFICO DEPENDE FUERTEMENTE DE DICCIONARIO... ENTONCES SI DICCIONARIO CAMBIA O SE MODIFICA ALGO, EL CODIGO DE CORRETOR SE VERA MUY AFECTADO

#ASI DEBE SER LA MANERA CORRECTA RESPETANDO EL PRINCIPIO
from abc import ABC, abstractclassmethod

class VerificadorOrtografico(ABC):
    @abstractclassmethod
    def verificar_palabra(self, palabra):
        #LOGICA PARA VERIFICAR PALABRA
        pass


class Diccionario(VerificadorOrtografico):
    def verificar_palabra(self, palabra):
    #LOGICA PARA VERIFICAR PALABRAS SI ESTA EN EL DICCIONARIO
        pass


class CorrectorOrtografico:
    def __init__(self, verificador):
        self.verificador = verificador
        
    def corregir_texto(self, texto):
        #USAMOS EL VERIFICADOR PARA CORREGIR EL TEXTO Y ASI NO USAMOS EL DICCIONARIO
        pass