# Supóngase que en una reciente elección hubo cuatro candidatos, con identificadores 1, 2, 3, 4. 
# Usted habrá de encontrar mediante un programa, el número de votos correspondiente a cada candidato y el porcentaje que obtuvo respecto al total de los votantes. 
# El usuario ingresara los votos de manera desorganizada, tal y como se obtuvieron en la elección, el final de datos está representado por un cero.
# Observe, como ejemplo, la siguiente lista.: 1 3 1 4 2 2 1 3 1 1 1 3 4 1 2 4 4 0


#Contador de votos para cada candidato:
votos1 = 0
votos2 = 0
votos3 = 0
votos4 = 0

print("Ingrese los votos (1 al 4). Ingrese 0 para cerrar.")

voto = int(input("Voto: "))

while voto !=0:
    if voto == 1:
        votos1 += 1
    elif voto == 2:
        votos2 += 1
    elif voto == 3:
        votos3 += 1
    elif voto == 4:
        votos4 += 1
    else:
        print("Voto inválido. ")
    voto = int(input("Voto: "))

#Calculo del total de votos:    
total_votos = votos1+votos2+votos3+votos4

#Calculo del porcentaje:
porcentaje1 = (votos1 / total_votos) * 100 if total_votos > 0 else 0
porcentaje2 = (votos2 / total_votos) * 100 if total_votos > 0 else 0
porcentaje3 = (votos3 / total_votos) * 100 if total_votos > 0 else 0
porcentaje4 = (votos4 / total_votos) * 100 if total_votos > 0 else 0

#Resultados:
print("\nRESULTADOS: ")
print("Candidato 1: ", votos1, "votos -", round(porcentaje1, 2), "%")
print("Candidato 2: ", votos2, "votos -", round(porcentaje2, 2), "%")
print("Candidato 3: ", votos3, "votos -", round(porcentaje3, 2), "%")
print("Candidato 4: ", votos4, "votos -", round(porcentaje4, 2), "%")