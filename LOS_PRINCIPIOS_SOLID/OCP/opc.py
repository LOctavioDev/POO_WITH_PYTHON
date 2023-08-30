#EL OPEN/CLOSE PRINCIPLE... NOS DICE QUE LAS ENTIDADES DE SOFTWARE (CLASES,MODULOSFUNCIONES,ETC) TIENE QUE ESTAR ABIERTAS PARA LA EXTENCION PERO CERRADAS PARA LA MODIFICACION
#VAMOS A CREAR UN SISTEMA QUE ENVIE NOTIFICACIONES A LOS USUARIOS

class Notificador:
    def __init__(self, usuario, mensaje):
        self.usuario = usuario
        self.mensaje = mensaje
    
    def notificar(self):        #ESTAMOS CREANDO UNA CLASE PADRE QUE NOS OBLIGUE A DECIRLE AL DESARROLLADOR QUE TIENE QUE CREAR LA CLASE NOTIFICAR
        raise NotImplementedError


class NotificadorEmail(Notificador):
    def Notificar(self):
        print('ENVIANDO EMAIL A {self.usuario.email}')

        
class NotificadorSMS(Notificador):
    def Notificar(self):
        print('ENVIANDO SMS A {self.usuario.sms}')
        

class NotificadorWhatsApp(Notificador):
    def Notificar(self):
        print('ENVIANDO UN WHATS A {self.usuario.whatsapp}')
        

class NotificadorX(Notificador):
    def Notificar(self):
        print('ENVIANDO UN X A {self.usuario.X}')
        
#CREAMOS UN PROGRAMA QUE PUEDE SER EXTENSIBLE ES DECIR, ESTA ABIERTO A AGREGAR FUNCIONALDADES NUEVAS 