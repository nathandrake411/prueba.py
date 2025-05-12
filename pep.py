canciones = ["diles", "llueve sobre la ciudad", "eut", "oda"]

#for cancion in canciones:
    #print(cancion)
    #print(cancion())

acumulador = 0


print(len( canciones))
for cancion in canciones:
    acumulador = acumulador + 1
    print(canciones[ len(canciones) - acumulador ])