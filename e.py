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
    
    res = re.search(r'<nome>([\w\s]+)<\/nome>',dados).group(1)
    if(res):
        lista.append(res)

    res = re.search(r'<pai\/>',dados)
    if(res):
        lista.append("?")

    else:
        res = re.search(r'<pai>([\w\s]+),?.*<\/pai>',dados).group(1)
        if(res):
            lista.append(res)

    res = re.search(r'<mae\/>',dados)
    if(res):
        lista.append("?")

    else:
        res = re.search(r'<mae>([\w\s]+),?.*<\/mae>',dados).group(1)
        if(res):
            lista.append(res)

    return lista
    

def procurarDados(conteudo, ano):
    dot = Graph(comment='Arvore genealogica')
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
                    mae = lista[3] + " (mae)"
                    pai = lista[2] + " (pai)"
                    filho = lista[1] + " (filho)"
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