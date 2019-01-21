#Autor: Alan Giovanni Rodriguez Camacho
#Calcula la velocidad promedio de un viaje

Tiempo=float(input("¿Cuanto fue el tiempo que duro tu viaje realizado en minutos?: "))
Distancia=float(input("¿Cual fue la distancia en metros que recorriste en tu viaje?: "))

Vel= Distancia/Tiempo

print("Tu velocidad promedio al recorrer {0} m en {1} min fue: {2} m/s".format(Distancia,Tiempo,Vel))