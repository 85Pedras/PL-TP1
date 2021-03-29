import sys
import re

def delete(lista,x):
    while (x in lista):
        lista.remove(x)

def auxOrd(elem):
    return elem[1]


f = open ("processos.xml",encoding="utf8")
conteudo = f.read()



#Número de processos por ano
anos = re.findall(r'<data>(\d{4})-\d{2}-\d{2}<\/data>',conteudo)
#for elem in anos:
#    print(f'Número de processos no ano {elem} = {anos.count(elem)}')
#    delete(anos,elem)



#Lista de processos por ordem cronologica
processos = re.findall(r'<processo id="(\d+)">\n.+\n.+<data>(\d{4}\-\d{2}\-\d{2})<\/data>\n.+\n.+\n.+\n.+\n.+<\/processo>', conteudo)
processos.sort(key=auxOrd)
#print("Processos ordenados: ")
#for elem in processos:
#    print(elem[0])



#Intervalo de datas
data_inicial = (processos[0][1])
data_final = (processos[len(processos)-1][1])

print(f'Intervalo de datas: {data_inicial} <=> {data_final}')


#Número de séculos
seculos = []
for elem in anos:
    if res := re.match(r'(\d+)00',elem):
        sec = int(res[1])
        if (sec in seculos) == False:
            seculos.append(sec)

    elif res := re.match(r'(\d+)\d{2}',elem):
        sec = int(res[1])+1
        if (sec in seculos) == False:
            seculos.append(sec)

print(seculos)
print(f'Número de séculos analisados: {len(seculos)}')
f.close()
