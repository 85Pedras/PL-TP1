import sys
import re

f = open ("processos.xml",encoding="utf8")
conteudo = f.read()
processos = re.findall(r'<processo id.+\n.+\n.+\n.+<nome>((\w+).* (\w+))<\/nome>\n.+\n.+\n.+\n.+<\/processo>',conteudo)

print(processos[0])