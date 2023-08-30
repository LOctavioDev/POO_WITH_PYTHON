from textblob import TextBlob

class AnalizadorDeSentimientos:
    def analizar_sentimiento(self, texto):
        analisis = TextBlob(texto)
        if analisis.sentiment.polarity > 0:
            return 'Positivo'
        
        elif analisis.sentiment.polarity == 0:
            return 'Neutral'

        else:
            return 'Negativo'
        
analizador = AnalizadorDeSentimientos()
resultado = analizador.analizar_sentimiento("Hello I'm very Sad")

print(resultado)

#ESTO NO ES TAN PRESICIO.... SI, USA IA PERO NO ES TAN PRECISO