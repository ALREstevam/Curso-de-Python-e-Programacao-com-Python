pontos = 0
answers = ['a', 'b', 'a', 'c', 'd']
questao = 0

while questao < len(answers):
    resposta = str(input('Resposta da questão {} (a, b, c, d, e) : '.format(questao+1))).lower()

    if resposta == answers[questao]:
        pontos = pontos + 1

    questao = questao + 1

print('O aluno fez {}/{} ponto(s)'.format(pontos, len(answers)))