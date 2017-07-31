#Desafio 8 - Converter de m para cm e mm

medidam = float(input("Digite um valor em metros: "))

print(
    '{:.2f} m = \n'
    '[{:.5f} km]\n'
    '[{:.2f} hm]\n'
    '[{:.2f} dam]\n'
    '[{:.0f} dm]\n'
    '[{:.0f} cm]\n'
    '[{:.0f} mm]\n'
        .format(
                medidam,
                medidam / 1000,
                medidam / 100,
                medidam / 10,
                medidam * 10,
                medidam * 100,
                medidam * 1000
                )
    )
