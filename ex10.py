name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fh = open(name)                                     #abre o file 
counts = dict()                                     #cria o dicioário 

for line in fh:                                     #le de linha em linha 
    line = line.rstrip()                            #separa as linhas e tira todos os white spaces
    if not line.startswith('From ') : continue      #se nao começar com 'From: ' reinicia o laço
    words = line.split()                            #separa as palavras da linha
    word = words[1]                                 #pega a 2 palavra (email)
    counts[word] = counts.get(word, 0) + 1          #coloca a palavra no dicionário se ainda não tiver e soma 1, se tiver apenas soma 1

biggest = None
sender = None                                       #inicialização das variáveis 
for word, count in counts.items():                  #varre cada uma das palavras e valores no dicionário
    if biggest is None or count > biggest:          #caso a variável que verifica o maior valores estiver inciializada co None ou caso o número atual seja maior do que o ultimo numero registrado
        sender = word 
        biggest = count

print (sender, biggest)
