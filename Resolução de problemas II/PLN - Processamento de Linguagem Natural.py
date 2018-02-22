"""
# Processamento de Linguagem Natual (PLN)
## Problemas
Desambiguação: o significado de uma palavra depende do contexto

Dish e Serve tem diferentes significados a depender do contexto

**Advérbios**
... by the searches (agente)
... by the moutain (local)
... by the afternoon (tempo)

by tem vários significados

**Detecção de sujeito e objetos de verbos**
Descobrir quem fez o que para quem

"the thieves stole the paintings. They were found" QUEM?

**Geração automática de texto**
Gerar texto a partir de dados brutos não linguísticos

* Tradução automática de alta qualidade
    * Diferentes traduções
    * Diferentes ordens
    * Diferentes estruturas linguísticas

"""

"""
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
    raw = text6[:]
    inicio = raw.index(“SCENE”)
    fim = raw.index(“SCENE”,inicio+1)
    scene_one = text6[inicio, fim]
    # Separa em sentenças
    sentences = sent_tokenize(scene_one)
    # Realiza tokenização da quarta sentença
    tokenized_sent = word_tokenize(sentences[3])
    # Cria um conjunto de tokens únicos
    unique_tokens = set(word_tokenize(scene_one))
    # imprime os tokens
    print(unique_tokens)

import nltk, re, pprint
from bs4 import BeautifulSoup
import urllib.request
url = “https://twitter.com/comp_science”
html = urllib.request.urlopen(url) # abre url
html_doc = html.read() # lê url

# cria objeto Beautiful Soup
soup = BeautifulSoup(html_doc, 'html.parser')
text = soup.get_text()

from nltk.tokenize import regexp_tokenize
from nltk.tokenize import TweetTokenizer
Use as funções reexp_tokenize e TweetTokenizer para:

• Encontrar todos os links postados em um endereço do Twitter em particular.
• Teste o r"([#|@]\w+)“ em um twitter, o que ele retorna?
• Encontrar todos os ‘#’ de um twitter. É possível descobrir o tópico do twitter?
• A expressão a seguir, encontra emojis, use-a para encontrar e imprimir emojis em um twitter.
- emoji = "['\U0001F300-\U0001F5FF'|'\U0001F600-\U0001F64F'|'\U0001F680-\U0001F6FF'|'\u2600-
\u26FF\u2700-\u27BF']



python
from nltk.tokenize import regexp_tokenize
from nltk.tokenize import TweetTokenizer
import nltk, re, pprint
from bs4 import BeautifulSoup
import urllib.request
url = “https://twitter.com/comp_science”
html = urllib.request.urlopen(url)
html_doc = html.read()
tok = TweetTokenizer()
tokenizedtxt = tok.tokenize(text)

def findintxt(text, subs):
    for elem in text:
        if subs in elem:
            print(elem)

findintxt(tokenizedtxt, 'http://')
findintxt(tokenizedtxt, '@')
findintxt(tokenizedtxt, '#')

str1 = ''.join(text1)

import re
matchstr = '([#|@]\w+)'
re.findall(matchstr, str1)

matchstr = '([#]\w+)'
re.findall(matchstr, str1)

emoji = "['\U0001F300-\U0001F5FF'|'\U0001F600-\U0001F64F'|'\U0001F680-\U0001F6FF'|'\u2600-\u26FF\u2700-\u27BF']"

re.findall(emoji, str1)

"""

