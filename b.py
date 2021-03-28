import sys
import re

def pertence(elem,lista):
    for x in lista:
        if x == elem:
            return True
    return False

def delete(lista,x):
    while pertence(x,lista):
        lista.remove(x)

nomes = []
apelidos = []
f = open ("processos.xml",encoding="utf8")
conteudo = f.read()
processos = re.findall(r'<processo id.+\n.+\n.+\n.+<nome>((\w+).* (\w+))<\/nome>\n.+\n.+\n.+\n.+<\/processo>',conteudo)
#for p in processos:
#    ps.append(list(p))

auxprocessos = processos
for elem in auxprocessos:
    n = elem[1]
    a = elem[2]
    nomes.append(n)
    apelidos.append(a)

nomesOrd = []
apelidosOrd = []

for nome in nomes:
    k = nomes.count(nome)
    nomesOrd.append([nome,k])
    delete(nomes,nome)

for apelido in apelidos:
    k = apelidos.count(apelido)
    apelidosOrd.append([apelido,k])
    delete(apelidos,apelido)

print(nomesOrd)




