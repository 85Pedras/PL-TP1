from graphviz import Graph 
import re

ids = set() #todos os ids dos processos ja encontrados

def lerDados(dados,ano):
    lista = []
    res = re.search(r'<data>(\d{4})-.+<\/data>',dados).group(1)
    if(res and int(res) == ano):
        lista.append(res)
    else:
        return lista

    res = re.search(r'<nome\/>',dados)
    if(res):
        lista.append("?")
    
    res = re.search(r'<nome>([\w\s]+)<\/nome>',dados)
    if(res):
        lista.append(res.group(1))

    res = re.search(r'<pai\/>',dados)
    if(res):
        lista.append("?")

    else:
        res = re.search(r'<pai>([\w\s]+),?.*<\/pai>',dados)
        if(res):
            lista.append(res.group(1))

    res = re.search(r'<mae\/>',dados)
    if(res):
        lista.append("?")

    else:
        res = re.search(r'<mae>([\w\s]+),?.*<\/mae>',dados)
        if(res):
            lista.append(res.group(1))

    return lista
    

def procurarDados(conteudo, ano):
    dot = Graph(comment='Arvore genealogica', format='png')
    count = 0
    res = re.findall(r'<processo id="(\d+)">\n\s+(.+\n.+\n.+\n.+\n.+\n.+)\n.+<\/processo>',conteudo)
    if res:
        for (idProcesso,dados) in res:
            if(not idProcesso in ids):
                ids.add(idProcesso)
                lista = lerDados(dados,ano)
                if(len(lista) > 0): #Construcao da arvore genealogica
                    count = count + 1
                    countStr = str(count)
                    dot.attr('node', shape='box')
                    if(len(lista) > 3):
                        mae = lista[3] + " (mae)"
                    else:
                        mae = "?"
                    if(len(lista) > 2):
                        pai = lista[2] + " (pai)"
                    else:
                        pai = "?"
                    if(len(lista) > 1):
                        filho = lista[1] + " (filho)"
                    else:
                        filho = "?"
                    dot.node(mae,mae)
                    dot.node(pai,pai)
                    dot.node(filho,filho)

                    dot.attr('node', shape='point')
                    dot.node(countStr)

                    dot.edge(mae,countStr,constraint='false')
                    dot.edge(pai,countStr,constraint='false')
                    dot.edge(countStr,filho)
                else:
                    pass
            else:
                pass
    
    if(count > 0):
        dot.render(str(ano) + ".gv",view=True)

#Abrir o ficheiro
f = open("processos.xml")
conteudo = f.read() #Ler tudo
ano = int(input("Introduza o ano >> "))
procurarDados(conteudo, ano)
f.close()