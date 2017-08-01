cigarroDia = int(input("Cigarros fumados por dia: "))
tempoFumante = int(input("Há quantos anos fuma?\n: "))

perdaCigarro = 10
cigarrosTotais = 365 * tempoFumante * cigarroDia

perdaMinutos = cigarrosTotais * perdaCigarro
perdaDias = perdaMinutos / 1440

print("Fumando {} cigarros por dia duarante {} anos, foram fumados {} "
      "cigarros e houve uma perda de {} dias na expectativa"
      "de vida".format(cigarroDia, tempoFumante, cigarrosTotais, perdaDias))

# 1d = 24h = 60*24 min = 1440 min
