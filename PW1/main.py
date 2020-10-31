import os
import threading
import time

class Cpu:
    def __init__(self,idProgram,idMem,contadorPC,fatiaTempo,unidadeTempo):
        self.idProgram = idProgram
        self.idMem = idMem
        self.contador = contadorPC
        self.fatiaTempo = fatiaTempo
        self.unidadeTempo = unidadeTempo

    def imprime(self):
        print(self.idProgram)


class Processos:
    def __init__(self,id,idParent,pointerPC,vetorEstruturaDados,prioridade,estado,inicio,tempoCpu):
        self.id = id
        self.idParent = idParent
        self.pointerPC = 0
        self.vetorEstruturaDados = vetorEstruturaDados
        self.prioridade = prioridade
        self.estado = estado
        self.inicio = inicio
        self.tempoCpu = tempoCpu


class Gerenciador(Cpu,Processos):
    def __init__(self,tempo,cpu,tabProcess,estadoP,estadoB,estadoE):

        self.tempo = 0
        self.cpu = cpu
        self.tabProcess = tabProcess
        self.estadoP = estadoP
        self.estadoB = estadoB
        self.estadoE = estadoE

    def newProcess(self):

class Processo_simulado:
    def __init__(self):
        self.name = "asdasd"

    def ler(self):
        

    # def subProcess(self):
    #
    # def transicaoProcess(self):
    #
    # def escalonar(self):
    #
    # def trocar(self):

#
# def entrada():
#     print("[*] Metodo de entrada de dados")
#     print("[0] Entrada padrao")
#     print("[1] Arquivo")
#     op = int(input())
#     if(op==0):
#         print("Selecionado -> Entrada padrao")
#     if(op==1):
#         print("Selecionado -> Arquivo")
#     return op
#
# def lread(re):
#
#     while True:
#         # r = os.fdopen(re)
#         print("ok")
#         # print("Texto lido: ",r.read())
#
#
#
# print("TESTANDO")
# re, write = os.pipe()
# pid = os.fork()
# x=0
#
#
# # PROCESSO CONTROLE
#
# text = ""
#
# if(pid> 0):
#     os.close(re)
#     print("Parent escrevendo...")
#
#     while text != "M":
#         text = raw_input()
#         os.write(write,text+";")
#         print("Texto enviado: ",text)
#
#     print("PID pai: , ",os.getpid())
#
#
# # GERENCIADOR DE PROCESSOS
# if(pid == 0):
#     os.close(write)
#     print("Child esta lendo...")
#
#     print("PID filho: ",os.getpid())
#
#     r = os.fdopen(re)
#     text = r.read()
#     print("Texto lido: ",text)
#     text = text.split(";")
#     text.remove('')
#     print(text)
#

cpu = Cpu(0,0,0,0,0)
cpu.imprime()
cpu.idProgram = 5
cpu.imprime()
gerenciador = Gerenciador(0,0,0,0,0,0)



    #
