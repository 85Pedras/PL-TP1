import sys
import re

def delete(lista,x):
    while (x in lista):
        lista.remove(x)

def auxOrd(elem):
    return elem[1]


f = open ("processos.xml",encoding="utf8")
conteudo = f.read()


#MÃES
# Lista de mães
maes = re.findall(r'<mae>(.*)<\/mae>',conteudo)

# Lista de mães ordenadas
maes_ord = sorted(maes)

# Lista de mães repetidas
mae_repetida = []
for mae in range(len(maes_ord)):
    if maes_ord[mae] == maes_ord[mae-1]:
        if not maes_ord[mae] in mae_repetida:
            mae_repetida.append(maes_ord[mae])

for mae in range(len(mae_repetida)):
    print(f'A {mae_repetida[mae]} tem mais do que um filho candidato.')

print(f'Existem {len(mae_repetida)} mães que têm mais do que um filho candidato.')

# Verificar se uma mãe tem mais do que um filho candidato
while True:
    mae = str(input("Insira o nome de uma mãe: "))
    i = 0
    for i in range(len(mae_repetida)):
        if mae_repetida[i] == mae:
            print(f'A mãe {mae_repetida[i]} tem mais do que um fiho candidato.')


#PAIS
# Lista de pais
pais = re.findall(r'<pai>(.*)<\/pai>',conteudo)

# Lista de pais ordenados
pais_ord = sorted(pais)

# Lista de mães repetidas
pai_repetido = []
for pai in range(len(pais_ord)):
    if pais_ord[pai] == pais_ord[pai-1]:
        if not pais_ord[pai] in pai_repetido:
            pai_repetido.append(pais_ord[pai])

for pai in range(len(pai_repetido)):
    print(f'O {pai_repetido[pai]} tem mais do que um filho candidato.')

print(f'Existem {len(pai_repetido)} pais que têm mais do que um filho candidato.')

# Verificar se uma mãe tem mais do que um filho candidato
while True:
    pai = str(input("Insira o nome de um pai: "))
    i = 0
    for i in range(len(pai_repetido)):
        if pai_repetido[i] == pai:
            print(f'O pai {pai_repetido[i]} tem mais do que um fiho candidato.')


f.close()
