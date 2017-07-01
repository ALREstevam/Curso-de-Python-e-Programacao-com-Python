#Desafio 4

n = input("Digite algo: ")
print(
      '# Tipo primitivo:        {}\n'
      '# É numérico:            {}\n'
      '# É alfabético:          {}\n'
      '# É alfanumérico:        {}\n'
      '# É uppercase apenas:    {}\n'
      '# É lowercase apenas:    {}\n'
      '# Está captalizada:      {}\n'
      '# Só tem espaços:        {}\n'
      .format(
        type(n),
        n.isnumeric(),
        n.isalpha(),
        n.isalnum(),
        n.isupper(),
        n.islower(),
        n.istitle(),
        n.isspace()
      )
)
