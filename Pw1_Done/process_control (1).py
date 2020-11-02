import os, sys
from pai_de_todos import *

# -*- coding: UTF-8 -*-

  #funcao parente tambem pode criar um filho

r,w = os.pipe()
#
# def func(x):
#     print(x)
#     x = x[0]
#     print(x)
#     return x
os.system("clear")
print(" Processo Controle em execução...\n")
print(" Simulação: Gerenciamento de Processo")
print(" Métodos: ")
print("  [*] 1. Arquivo")
print("  [*] 2. Entrada Manual")
# decision = 1
decision = int(input("\n  => "))



if decision == 1:
    pid = os.fork()
       #assume-se que o processo controle  apenas pai
    pas_file = b" "

    if pid == 0:
        # time.sleep(2)
        os.close(w)
        # print("Child esta lendo...")
        # print("PID filho: ",os.getpid())
        r = os.fdopen(r)
        text = r.read()

        aux = str(text)
        # print("TEXTO PR:",aux[0])
        aux2 = "".join(list(map(lambda x:x+",",text)))
        aux2 = aux2[0:len(aux2)-1]
        print("Comando: ",aux2)


        gerenciador = Gerenciador()

        for i in range(len(text)):
            gerenciador.le_entrada(text[i])


        print("  [*] Tempo final do gerenciado", gerenciador.tempo_atual)

    if pid > 0:

        os.close(r)
        f = open("../Comandos.txt", "r")
        line = f.readlines()
        # print(line)
        lista = []
        for i in line:
            lista.append(i)
        lista2 = list(map(lambda x:x[0],lista))
        # print(lista2)
        for text in lista2:
            # print("Parent process is writing")
            os.write(w, text.encode())
            # print("Written text:", text)




if decision == 2:
    pid = os.fork()
       #assume-se que o processo controle  apenas pai
    pas = b" "
    if pid > 0:
        os.close(r)
        print(" Entrada de Comando\n")
        print("  [*] U: Fim de uma unidade de tempo.")
        print("  [*] L: Inícia processo que estava bloqueado.")
        print("  [*] I: Imprime o tempo médio do ciclo.")
        print("  [*] M: Imprime o tempo médio do ciclo e finaliza o sistema.\n")
        answer = str(input("  => "))
        if(answer == "M"):
            pas = b"M"
            os.write(w, pas)
        while answer != "M":
            if answer == "U":
                pas = b"U"
            elif answer == "L":
                pas = b"L"
            elif answer == "I":
                pas = b"I"
            elif answer == "M":
                pas = b"M"
            text = pas
            os.write(w, pas)
            # print("Parent process is writing")
            # print(":", text.decode())
            # print("Digite um dos comando para o processo controle executar alguma operacao:\n")
            answer = str(input("  => "))
            if(answer == "M"):
                pas = b"M"
                os.write(w, pas)


    if pid == 0:
        os.close(w)
        # print("Child esta lendo...")
        # print("PID filho: ",os.getpid())
        r = os.fdopen(r)
        text = r.read()

        aux = str(text)
        # print("TEXTO PR:",aux[0])
        aux2 = "".join(list(map(lambda x:x+",",text)))
        aux2 = aux2[0:len(aux2)-1]
        print("  Comando: ",aux2)

        gerenciador = Gerenciador()

        for i in range(len(text)):
            gerenciador.le_entrada(text[i])


        print("Tempo final do gerenciado", gerenciador.tempo_atual)




#
#
#
# while text != "":
#     comando = text[0]
#     print(text)
#     text = text.replace(comando,'',1)
#     index = 0
#     if (comando == "U"):
#         for process in gerenciador.tabProcess:
#             if(process.prioridade == 0):
#                 # process.execute()
#             index +=1
