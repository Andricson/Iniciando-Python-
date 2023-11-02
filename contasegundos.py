num = int(input("Por favor, entre com o número de segundos que deseja converter:"))
dia = num//86400
seg_rest1 = num%86400
hora = seg_rest1//3600
seg_rest2 = seg_rest1%3600
minutos = seg_rest2//60
seg_rest3 = seg_rest2%60
print(dia,"dias,",hora,"horas,",minutos,"minutos e",seg_rest3,"segundos.")