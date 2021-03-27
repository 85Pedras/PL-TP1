import sys
import re

def delete(lista,ano):
    for elem in lista:
        if elem[2] == ano:
            lista.remove(elem)

def auxOrd(elem):
    return elem[1]

def pertence(elem,lista):
    for x in lista:
        if x == elem:
            return True
    return False


f = open ("processos.xml",encoding="utf8")
conteudo = f.read()
processos = re.findall(r'<processo id="(\d+)">\n.+\n.+<data>((\d{4})\-\d{2}\-\d{2})<\/data>\n.+\n.+\n.+\n.+\n.+<\/processo>', conteudo)


#Número de processos por ano
processos_ano = processos
for elem in processos_ano:
    ano = elem[2]
    print(f'Número de processos no ano {ano} = {processos_ano.count(elem)}')
    delete(processos_ano,ano)


#Lista de processos por ordem cronologica
processos.sort(key=auxOrd)
print("Processos ordenados: ")


#Intervalo de datas
for elem in processos:
    print(elem[0])
data_inicial = int(processos[0][2])
data_final = int(processos[len(processos)-1][2])

print(f'Intervalo de datas: {data_inicial} - {data_final}')


#Número de séculos
seculos = []
for elem in processos:
    if res := re.match(r'(\d+)00',elem[2]):
        sec = res[1]
        if pertence(sec,seculos) == False:
            seculos.append(sec)
            
    elif res := re.match(r'(\d+)\d{2}',elem[2]):
        sec = res[1]
        if pertence(sec,seculos) == False:
            seculos.append(sec)
            

print(f'Número de séculos analisados: {len(seculos)}')
f.close()
