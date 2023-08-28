#EN POCAS PALABRAS UN DECORADRO EN UNA FUNCION ESPECIAL QUE DECORA A OTRAS... ES DECIR ... ES UNA FUCNION QUE AGREGA UN CODIGO EXTRA A LA FUNCION QUE YA EXISTIA PUEDE SER ANTES O DESPUES

def decorador(funcion): #ESATMOS CREANO UNA FUNCION DECORADORA QUE NOS VA A PEDIR COMO PAAMETRO UNA FUNCION
    def funcion_modificada():
        print('Antes de llamar a la funcion')
        funcion()
        print('Despues de llamar a la funcion')
    
    return funcion_modificada


# def saludo():
#     print('Holi...')
    

# saludo_modificado = decorador(saludo)
# saludo_modificado()

#---------CODIGO OPTIMO---------#

@decorador
def saludo():
    print('Holi...')
    
saludo()