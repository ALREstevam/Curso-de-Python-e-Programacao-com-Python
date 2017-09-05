'''

class <NomeDaClasse>:
 """Descição da classe""" # acessada por print NomeDaClasse__.doc__


    CONSTRUTOR

    def __init__(self):
    """..."""
    ...

    Time.__init__.__doc__

    Atributos começando com  _, indica que não devem ser acessados diretamente

    self._hour = 0

    pois existe setHour(...):


    python permite:

    if 0 <= hour < 24: (hora entre 0 e 24)

    EXCEÇÕES

    raise <tipo de exceção>, "Mensagem de erro"


    DESTRUTORES
    __del__
    executa quando não há mais referência ao objeto


    ATRIBUTOS DA CLASSE
    class NomeDaClasse:
        atributoDaClasse = 0

        def __init__(self):
            ...


        def __del__(self):
            Empregado.contador -= 1



    nomedaclasse1 = nomedaclasse0 # cria um alias para nomedaclasse0
    del nomedaclasse1


    COMPOSIÇÃO

    self.birthDate = Date(day, month, year)

'''
import random

class Foo:
    def __init__(self):
        print('Fui iniciado')

    def test(self):
        a = 0
        raise(ValueError, 'Errow')

    def wakeup(self):
        print('Oi')


f1 = Foo()
f1.wakeup()
#f1.test()

random.seed(1)

for i in range(20):
    print(random.randint(0,5))