dias = int(input("Dias: "))
horas = int(input("Horas: "))
minutos = int(input("Minutos: "))
segundos = int(input("Segundos: "))

# 1 min = 60 sec
# 60 min = 1h
# 24h = 1d

# 1d = 24h
# 24h = 24h * 60min = 1440min
# 1440 min = 1440 * 60 sec = 86400

diasParaSegundos = dias * 86400
horasParaSegundos = horas * 1440
minutosParaSegundos = minutos * 60

print("{}dias, {}h, {}min, {}s = {}s".format(dias, horas, minutos, segundos, (diasParaSegundos+horasParaSegundos+minutosParaSegundos+segundos) ))