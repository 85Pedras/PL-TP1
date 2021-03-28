import sys
import re

def auxOrd(elem):
    return elem[1]

def delete(lista,x):
    while (x in lista):
        lista.remove(x)

f = open ("processos.xml",encoding="utf8")
conteudo = f.read()

nomes = re.findall(r'<nome>(\w+).* \w+<\/nome>',conteudo)
apelidos = re.findall(r'<nome>\w+.* (\w+)<\/nome>',conteudo)

nomesOrd = []
apelidosOrd = dict()

#for nome in nomes:
    #k = nomes.count(nome)
    #nomesOrd.append([nome,k])
    #delete(nomes,nome)

#nomesOrd.sort(key=auxOrd,reverse=True)

for apelido in apelidos:
    if (apelido in apelidosOrd):
        apelidosOrd[apelido] += 1
    else:
        apelidosOrd[apelido] = 1

    #x = apelidos.count(apelido)
    #apelidosOrd.append([apelido,x])
    #delete(apelidos,apelido)

#apelidosOrd.sort(key=auxOrd,reverse=True)

#print(nomesOrd)

#print(apelidosOrd)

for elem in sorted(apelidosOrd,key=apelidosOrd.get,reverse=True):
    print(elem,apelidosOrd[elem])


