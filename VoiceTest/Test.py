mysp=__import__("my-voice-analysis") # importamos la libreria de python
#funcion que retornara el rango etario y el genero de una persona
def Rango( genero ,frecuencia):
    if(genero == 'hombre'):
        if (frecuencia <= 121.5 and frecuencia >110):
            print("es Hombre Adolecente")
        if(frecuencia > 121.95 and frecuencia <=127):
            print("es Hombre Adulto")
        #encontrar la relacion
        if(frecuencia > 127.5 and frecuencia < 164):
            print("es Hombre anciano")
        elif (frecuencia > 155):
            print("es niño Hombre")
    if (genero == 'mujer'):
        if (frecuencia <= 224.58 and frecuencia >196.31):
            print("es Mujer Adolecente")
        if(frecuencia <=196.31  and frecuencia >178.92):
            print("es Mujer Adulto")
        #encontrar la relacion
        if(frecuencia <= 178.92 ):
            print("es Mujer anciana")
        elif (frecuencia > 200):
            print("es niña ")



p="male001" #nombre del archivo wav
c=r"/home/seba/Escritorio/VoiceTest/" #ubicacion de la carpeta

x=mysp.myspgend(p,c) #asignamos el genero
y=mysp.myspf0med(p,c) #asignamos la frecuencia fundamental
Rango(x,y)




        #encontrar la relacion
#frecuencia fundamental global
#mysp.myspf0min(p,c)#frecuencia fundamental global minima
#mysp.myspf0max(p,c)#frecuencia fundamental global maxima
#mysp.myspf0q25(p,c)#frecuencia fundamental global del quintil 25
#mysp.myspf0q75(p,c)#frecuencia fundamental global del quintil 75
