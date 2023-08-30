# #EL LISKOV'S SUBSTITUTION PRINCIPLE... ESTABLECE QUE LAS CLASES DERIVADAS TIENE QUE SER SUSTITUIBLES POR SUS CLASES BASE 
# class Ave:
#     def volar(self):
#         return 'ESTOY VOLANDO'          #TODO LO QUE LA CLASE PRINCIPAL PUEDA HACER LA SUBCLASE TAMBIEN LO DEBE DE PODER HACER

# class Pinguino(Ave):
#     def volar(self):
#         return  'NO PUEDO VOLAR'
    
# def hacer_volar(ave = Ave):
#     return ave.volar()

# print(hacer_volar(Pinguino()))


class Ave:
    pass

class AveVoladora(Ave):
    def volar(self):
        return 'ESTOY VOLANDO'


class AveNoVoladora(Ave):
    pass