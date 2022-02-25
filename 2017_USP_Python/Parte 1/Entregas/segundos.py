segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))

dias = segundos // 86400
segundos_int = segundos % 86400
horas = segundos_int // 3600
segundos_int2 = segundos_int % 3600
minutos = segundos_int2 // 60
segundos_finais = segundos_int2 % 60

print(dias, "dias,", horas, "horas,", minutos, "minutos e", segundos_finais, "segundos.")
