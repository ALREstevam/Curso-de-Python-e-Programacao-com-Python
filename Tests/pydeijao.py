import requests as Rq
from bs4 import BeautifulSoup as Bs

link = 'http://www.pfl.unicamp.br/Rest/view/site/cardapio.php'
page = Rq.get(link)
soup = Bs(page.content, 'html.parser', from_encoding='iso-8859-1')

soup = Bs(page.content, 'html.parser')

def formatInput(text):
    text = text.replace('\n', '')
    text = text.replace('\r', '')
    text = text.replace(': ', ':')
    text = text.replace(' - ', '-')
    text = text.strip()
    return text

html = []

html.append(formatInput(soup.find_all('tr')[0].getText()))
for i in range(4, 11):
    html.append(formatInput(soup.find_all('tr')[i].getText()))

print('\n\n')
print('{:^50s}'.format(html[0].split('-')[0].upper()))
print()
print('{:^50s}'.format(html[0].split('-')[1]))
print('-'*57)


broke = []
for elem in html[2:11]:
    broke.append(elem.split(':'))

for tup in broke:
    for elem in tup:
        elem = formatInput(elem)

for tup in broke:
    print('| {:20s} | {:<30s} |'.format(tup[0], tup[1].lower()))

print('-'*57)

input()