import
import re
strOrig = '''João amava Teresa que amava Raimundo
que amava Maria que amava Joaquim que amava Lili
que não amava ninguém.
João foi pra os Estados Unidos, Teresa para o convento,
Raimundo morreu de desastre, Maria ficou para tia,
Joaquim suicidou-se e Lili casou com J. Pinto Fernandes
que não tinha entrado na história.'''



matchstr = '[A-Z]\w+'
print('\nPROCURANDO NOMES COM "re.findall"')
print(re.findall(matchstr, strOrig))

#matchstr = '[A-Z](\.\s[A-S])?\w+'
matchstr = '([A-Z]\.\s)?[A-Z]\w+(\s[A-Z]\w+)*'
print('\nPROCURANDO NOMES COM "re.finditer"')
for m in re.finditer(matchstr, strOrig):
    print('{:<3}-{:>3}: {}'.format(m.start(), m.end(), m.group(0)))


print('\nPROCURANDO NOMES COMPOSTOS COM "re.finditer"')
matchstr = '([A-Z]\.\s)?[A-Z]\w+\s[A-Z]\w+'
for m in re.finditer(matchstr, strOrig):
    print('{:<4}-{:>4}: [ {:22}]'.format(m.start(), m.end(), m.group(0)))


print('CONTANDO CARACTERES')
print('Espaços: {}'.format(len(re.findall('[\s]',strOrig))))
print('Letras: {}'.format(len(re.findall('[\w]',strOrig))))
print('Palavras: {}'.format(len(re.findall('\w+',strOrig))))