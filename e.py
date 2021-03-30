from graphviz import Graph 
import re

def procurarDados(conteudo, ano):
    dot = Graph(comment='Arvore genealogica')
    count = 0
    res = re.findall(r'<data>(\d{4})-\d{2}-\d{2}<\/data>(.|\n)*?<nome>([\w\s]+)<\/nome>(.|\n)*?<pai>([\w\s]+)<\/pai>(.|\n)*?<mae>([\w\s]+)<\/mae>',conteudo)
    if res:
        for (a,_,n,_,p,_,m) in res:
            if(int(a) == ano):
                count = count + 1
                countStr = str(count)
                dot.attr('node', shape='box')
                dot.node(m,m)
                dot.node(p,p)
                dot.node(n,n)

                dot.attr('node', shape='point')
                dot.node(countStr)

                dot.edge(m,countStr,constraint='false')
                dot.edge(p,countStr,constraint='false')
                dot.edge(countStr,n)

        if(count > 0):
            dot.render('test.gv',view=True)


#Abrir o ficheiro
f = open("processos.xml")
conteudo = f.read() #Ler tudo

ano = int(input("Introduza o ano >> "))
procurarDados(conteudo, ano)