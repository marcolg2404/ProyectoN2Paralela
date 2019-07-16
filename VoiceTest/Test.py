mysp=__import__("my-voice-analysis") # importamos la libreria de python

p="female01" #nombre del archivo wav
c=r"/home/seba/Escritorio/VoiceTest/" #ubicacion de la carpeta

x=mysp.myspgend(p,c)
y=mysp.myspf0med(p,c)


print(x)
print(y)

#frecuencia fundamental global
#mysp.myspf0min(p,c)#frecuencia fundamental global minima
#mysp.myspf0max(p,c)#frecuencia fundamental global maxima
#mysp.myspf0q25(p,c)#frecuencia fundamental global del quintil 25
#mysp.myspf0q75(p,c)#frecuencia fundamental global del quintil 75
