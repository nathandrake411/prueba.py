from random import*

primer_numero = int(input("agrege el primer numero:"))
ultimo_numero = int(input("agrege el ultimo numero:"))



if primer_numero > ultimo_numero:
    print("error, primer numero debe de ser mayor que el ultimo")
    primer_numero = int(input("ingrese nuevamente el primer numero:"))

    punto_medio = (primer_numero + ultimo_numero) / 2

    ajuste_numero_aleatorio = (ultimo_numero - primer_numero) * 0.2
    numero_aleatorio_final = (randint(primer_numero, ultimo_numero))

    print(numero_aleatorio_final)

    #como puedo generar un numero aleatorio