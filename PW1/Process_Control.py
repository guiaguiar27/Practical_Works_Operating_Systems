import os
# -*- coding: UTF-8 -*-

  #funcao parente tambem pode criar um filho

r,w = os.pipe()
#
# def func(x):
#     print(x)
#     x = x[0]
#     print(x)
#     return x

print("Digite 1 para ler comandos de um arquivo\n 2 para digitar oscomandos")
decision = int(input())

if decision == 1:
    pid = os.fork()
       #assume-se que o processo controle  apenas pai
    pas_file = b" "
    if pid > 0:
        os.close(r)
        f = open("Comandos.txt", "r")
        line = f.readlines()
        print(line)
        lista = []
        for i in line:
            lista.append(i)
        lista2 = list(map(lambda x:x[0],lista))
        print(lista2)
        for text in lista2:
            print("Parent process is writing")
            os.write(w, text.encode())
            print("Written text:", text)

        # f.close()
    if pid == 0:
        os.close(w)
        print("Child esta lendo...")
        print("PID filho: ",os.getpid())
        r = os.fdopen(r)
        text = r.read()
        print("Texto lido: ",text)
        # pid  = parent()


if decision == 2:
    pid = os.fork()
       #assume-se que o processo controle  apenas pai
    pas = b" "
    if pid > 0:
        os.close(r)
        print("Digite um dos comando para o processo controle executar alguma operação:\nU: Fim de uma unidade de tempo.\n")
        print("L: Desbloqueia o primeiro processo simulado na fila bloqueada.\n")
        print("I: Imprime o estado atual do sistema.\n")
        print("M: Imprime o tempo médio do ciclo e finaliza o sistema.\n")
        answer = str(input(""))
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
            print("Parent process is writing")
            print("Written text:", text.decode())
            print("Digite um dos comando para o processo controle executar alguma operacao:\n")
            answer = str(input(""))


    if pid == 0:
        os.close(w)
        print("Child esta lendo...")
        print("PID filho: ",os.getpid())
        r = os.fdopen(r)
        text = r.read()
        print("Texto lido: ",text)
