import threading
import time
import os

class bcolors:
    Preto = '\033[1;30m'
    Vermelho = '\033[1;31m'
    Verde = '\033[1;32m'
    Amarelo = '\033[1;33m'
    Azul = '\033[1;34m'
    Magenta = '\033[1;35m'
    Cyan = '\033[1;36m'
    CinzaC = '\033[1;37m'
    CinzaE = '\033[1;90m'
    VermelhoC = '\033[1;91m'
    VerdeC = '\033[1;92m'
    AmareloC = '\033[1;93m'
    AzulC = '\033[1;94m'
    MagentaC = '\033[1;95m'
    CyanC = '\033[1;96m'
    Branco = '\033[1;97m'
    Negrito = '\033[;1m'
    Inverte = '\033[;7m'
    Reset = '\033[0;0m'





class Processo_simulado:
    def __init__(self, pid, paipid, pc, prioridade, estado, tempo_inicio, tempo_cpu, vetor_instrucoes, vetor_memoria, requisite, quantum):
        self.pid = pid
        self.paipid = paipid
        self.pc = pc
        self.vetor_memoria = vetor_memoria.copy()
        self.prioridade = prioridade
        self.estado = estado
        self.tempo_inicio = tempo_inicio
        self.tempo_cpu = tempo_cpu
        self.vetor_instrucoes = vetor_instrucoes.copy()
        self.requisite = requisite
        self.quantum = quantum
        self.tam = 0


class Cpu:
    def __init__(self, vetor_instrucoes, vetor_memoria, pc, tempo_cpu, pid, quantum_processo):
        self.vetor_instrucoes = vetor_instrucoes
        self.vetor_memoria = vetor_memoria
        self.pc = pc
        self.tempo_cpu = tempo_cpu
        self.pid = pid
        self.quantum_processo = quantum_processo

    def troca_processo(self, vetor_instrucoes, vetor_memoria, pc, tempo_cpu, pid, quantum_processo):
        self.vetor_instrucoes = vetor_instrucoes
        self.vetor_memoria = vetor_memoria
        self.pc = pc
        self.tempo_cpu = tempo_cpu
        self.pid = pid
        self.quantum_processo

    def le_instrucoes(self, nome_arquivo):
        f = open(nome_arquivo, "r")
        aux = f.readlines()
        return(aux)

    def executa_funcao(self):
        # print("INSTRU",self.vetor_instrucoes)
        # print("MEM",self.vetor_memoria,"PID",self.pid)
        if(self.vetor_instrucoes == []):
            return "O"
        # print("PC",self.vetor_instrucoes)
        # print("PC:",self.pc)
        # print("INS",self.vetor_instrucoes)
        line = self.vetor_instrucoes[self.pc].split()
        if line[0] == 'N':
            self.vetor_memoria = [0 for x in range(int(line[1]))]
            self.pc = self.pc + 1
        elif line[0] == 'D':
            self.pc = self.pc + 1
        elif line[0] == 'V':
            index = int(line[1])
            self.vetor_memoria[index] = int(line[2])
            self.pc = self.pc + 1
        elif line[0] == 'A':
            index = int(line[1])
            self.vetor_memoria[index] = self.vetor_memoria[index] + int(line[2])
            self.pc = self.pc + 1
        elif line[0] == 'S':
            index = int(line[1])
            self.vetor_memoria[index] = self.vetor_memoria[index] - int(line[2])
            self.pc = self.pc + 1
        elif line[0] == 'B':
            print(f"  {bcolors.Branco}[*]{bcolors.Reset} Bloqueia processo")
            self.pc = self.pc + 1
        elif line[0] == 'T':
            self.pc = self.pc + 1
        elif line[0] == 'F':
            print(f"  {bcolors.Branco}[*]{bcolors.Reset} Cria novo processo")
        elif line[0] == 'R':
            self.pc = 0
            self.vetor_instrucoes = self.le_instrucoes(line[1]) #substitui as instruções atuais pelas instruções no novo arquivo
        else:
            print("  [*] Arquivo com comando inválido")
            exit
        self.tempo_cpu += 1
        return(line)

    def retorna_valores(self):
        return( self.vetor_instrucoes, self.vetor_memoria, self.pc, self.tempo_cpu)



class Gerenciador(Cpu):
    def __init__(self):
        self.tabelaProcess = []
        self.tabela_pronto = []
        self.tabela_bloq = []
        self.tabela_final = []
        self.tabela_exec = []
        self.text = "U"
        self.tempo_atual = 0
        self.cpu = Cpu(0 ,0, 0, 0, 0, 1)
        self.newProcess_0('program_init.txt')
        self.processo_escalonado = 0

    def newProcess_0(self, nome_arquivo):
        vetor_instrucoes = self.cpu.le_instrucoes(nome_arquivo)
        processo = Processo_simulado(0, 0, 0, 0, 0, 0, 0, vetor_instrucoes, [], 0, 0.1)
        self.tabelaProcess.append(processo)
        # print("ANTES 1:",self.tabela_exec)
        self.tabela_pronto.append(0)
        # print("DEPOIS 1:",self.tabela_exec)
        self.insere_processo_cpu(processo.pid)

    def insere_processo_cpu(self, pid):

        for i in self.tabelaProcess:
            if i.pid == pid:

                self.tabela_exec.append(i.pid)
                # print("REMOVI a",self.tabela_pronto)
                self.tabela_pronto.remove(i.pid)
                # print("REMOVI d",self.tabela_pronto)
                vetor_instrucoes = i.vetor_instrucoes.copy()
                vetor_memoria = i.vetor_memoria.copy()
                pc = i.pc
                quantum = i.quantum
                i.estado = 2

        self.cpu.troca_processo(vetor_instrucoes, vetor_memoria, pc, 0, pid, quantum)

    def novos_valores_processo(self, estado):
        resultado = self.cpu.retorna_valores()
        pid = self.cpu.pid
        for i in self.tabelaProcess:
            if i.pid == pid:
                i.vetor_instrucoes  = resultado[0].copy()
                i.vetor_memoria = resultado[1].copy()
                i.pc  = resultado[2]
                i.tempo_cpu  += resultado[3]
                i.estado = estado


    def partition(self, process, low, high):
        i = (low-1)         # index of smaller element
        pivot = process[high].prioridade     # pivot
        for j in range(low, high):
            if process[j].prioridade <= pivot:
                i = i+1
                process[i].prioridade, process[j].prioridade = process[j].prioridade, process[i].prioridade

        process[i+1].prioridade, process[high].prioridade = process[high].prioridade, process[i+1].prioridade
        return (i+1)
    def quickSort(self, process, low, high):
        if len(process) == 1:
            return process
        if low < high:
            pi = self.partition(process, low, high)
            self.quickSort(process, low, pi-1)
            self.quickSort(process, pi+1, high)

    def initilize(self, processos):
        for i in processos:
            i.tempoCpu = 0.0
            i.blocked = 0.0
            i.requisite = 0
        return processos

    def escalonamento(self, processos):
        n = len(processos)
        self.quickSort(processos, 0, n-1)
        quantum = 1.0
        for i in processos:
            if i.prioridade == 0 :
                i.quantum = quantum
                if i.requisite == 1 : # o processo usou todo seu quantum para executar
                    i.quantum  = 2*quantum
                    i.prioridade = 1 #prioridade diminuida

            elif i.prioridade == 1:
                i.quantum = 2*quantum
                if i.requisite == 1 : # o processo usou todo seu quantum para executar
                    i.prioridade = 2 #prioridade diminuida
                if i.estado == 1 :
                    i.prioridade = 0

            elif i.prioridade == 2:
                i.quantum = 4*quantum
                if i.requisite == 1 : # o processo usou todo seu quantum para executar
                    i.prioridade = 3 #prioridade diminuida
                if i.estado == 1 :
                    i.prioridade = 1

            elif i.prioridade == 3:
                i.quantum = 8*quantum
                if i.estado == 1 :
                    i.prioridade = 2
        self.initilize(processos)
        return processos

    def troca_contexto(self):
            # print("LEN TROCA",len(self.tabela_bloq))
            if self.tabela_pronto != []:
                # print("LEN TROCA1",len(self.tabela_bloq))
                processos = self.tabelaProcess.copy()
                processos = self.escalonamento(processos)
                for i in processos:
                    if i.estado == 0:
                        # self.tabela_exec.append(i.pid)
                        self.insere_processo_cpu(i.pid)
                        # self.tabela_pronto.remove(i.pid)
                        # print("LEN TROCA2",len(self.tabela_bloq))
                        break
            elif self.tabelaProcess == []:
                # print("  [*] Não existem mais processos")
                self.cpu = None

    def le_entrada(self, comando):

            # comando = self.text[0]
            # print("-----------------------------------------------------------")
            # print("TABELA",len(self.tabelaProcess))
            # if(self.tabelaProcess != []):
            #     print("MEM",self.tabelaProcess[0].vetor_memoria)
            #     if(len(self.tabelaProcess) > 1):
            #         print("MEM2",self.tabelaProcess[1].vetor_memoria)
            # # print("TABELA2",self.tabelaProcess[1].vetor_instrucoes)
            # print("-----------------------------------------------------------")
            if (comando == "U" and self.tabelaProcess == []):
                print("  [*]  A tabela de processos está vazia!")
            if (comando == "U" and self.tabelaProcess != []):
                # print("TAMANHO:",len(self.tabelaProcess))
                # print("LEN",len(self.tabela_bloq))
                aux = self.cpu.executa_funcao()
                estado = 0
                # print("LINHA AUX",aux)
                # print("PROCESSO EM EXECUÇÃO: ",self.cpu.pid)
                if aux[0] == 'B':
                    estado = 1
                    # if(len(list(map(lambda x:x.pid==self.cpu.pid , self.tabelaProcess))) == 0):
                    #     print("EU EXISTO")
                    # print(self.tabela_pronto)
                    self.novos_valores_processo(estado)
                    self.tabela_bloq.append(self.cpu.pid)

                    self.tabela_exec.remove(self.cpu.pid)
                    # print("DEPOIS 3:",self.tabela_exec)

                    #ESCALONAMENTO É FEITO NO FINAL
                    # print("ESTOU BEM AQUI",self.cpu.vetor_instrucoes)

                    self.troca_contexto()
                elif aux[0] == 'T':

                    self.novos_valores_processo(4)

                    if(len(self.tabela_exec) != 0):
                        self.tabela_exec.pop(0)

                    for i in self.tabelaProcess:
                        if i.pid == self.cpu.pid:
                            index = self.tabelaProcess.index(i)
                            # print("ADICIONEI UM PROCESSO")

                            self.tabela_final.append(i)

                            self.tabelaProcess.remove(i)
                            # for i in range(len(self.tabela_bloq)):
                            #     if(self.tabela_bloq[i] > index):
                            #         # print("CHEGUEI")
                            #         self.tabela_bloq[i] = self.tabela_bloq[i] - 1
                            # self.tabela_bloq = list(map(lambda x: x-1 if x>index else False, self.tabela_bloq))


                    self.troca_contexto()
                elif aux[0] == 'F':
                    vetor_instrucoes = self.cpu.vetor_instrucoes.copy()
                    vetor_memoria = self.cpu.vetor_memoria.copy()
                    pc = self.cpu.pc + 1
                    tempo_cpu = 0
                    tempo_inicio = self.tempo_atual
                    novo_pid = self.cpu.pid + 1
                    paipid = self.cpu.pid
                    for i in self.tabelaProcess:
                        if i.pid == self.cpu.pid:
                            prioridade = i.prioridade
                    estado = 0
                    self.novo_processo(novo_pid, paipid, pc, prioridade, estado, tempo_inicio, tempo_cpu, vetor_instrucoes, vetor_memoria)
                    self.cpu.pc += int(aux[1]) + 1
                self.tempo_atual += 1

                if(aux[0] != 'B' and aux[0] != 'T'):
                    if (self.cpu.tempo_cpu == self.cpu.quantum_processo): #SE ISSO AQUI FOR TRUE O PROCESSO TEM QUE IR PRA PARTE DE PRONTO E PARAR DE EXECUTAR
                        # print("ENTREI AQUI DE ERRO")
                        for i in self.tabelaProcess:
                            if i == self.cpu.pid:
                                i.requisite = 1
                                self.novos_valores_processo(estado)
                                self.tabela_pronto.append(self.cpu.pid)
                                self.tabela_exec.remove(self.cpu.pid)
                                self.troca_contexto()
                                break

                # print("TEM PROCESSO",len(self.tabelaProcess))
            elif (comando =='L'):
                aux = self.tabela_bloq[0]
                # print("AUX",aux)
                if self.tabela_pronto == []:
                    self.tabela_pronto.append(aux)
                    self.tabela_bloq.pop(0)

                    for i in self.tabelaProcess:
                        if i.pid == aux:
                            i.estado = 0
                    self.troca_contexto()
                else:
                    self.tabela_pronto.append(aux)
                    self.tabela_bloq.pop(0)

                    for i in self.tabelaProcess:
                        if i.pid == aux:
                            i.estado = 0

            elif (comando == "I"):
                # print("  ------------------------------------------ Processos Prontos------------------------------------------------")
                print("  -----------")
                print(f"  {bcolors.Branco}[*]{bcolors.Reset} Processo Impressão Iniciado")
                print(f"\n\n  {bcolors.Amarelo}[*]{bcolors.Reset} Prontos\n")
                for i in self.tabela_pronto:
                    processo = list(filter(lambda x:x.pid == i,self.tabelaProcess))
                    process = processo[0]

                    print(f"  {bcolors.Branco}PID:{bcolors.Reset}",process.pid)
                    print(f"  {bcolors.Branco}PID parent:{bcolors.Reset}",process.paipid,end="")
                    print(f"\n  {bcolors.Branco}Tempo gasto:{bcolors.Reset}",process.tempo_cpu,end="")
                    print(f"\n  {bcolors.Branco}Instruções executadas:{bcolors.Reset}"," : ".join(list(map(lambda x:x.replace("\n",""), process.vetor_instrucoes))),end="")
                    print(f"\n  {bcolors.Branco}Memória:{bcolors.Reset}",process.vetor_memoria,end="")
                    print(f"\n  {bcolors.Branco}-----------")

                print(f"  {bcolors.Amarelo}-----------------------------------------------------------------------------------------------------------------------{bcolors.Reset}\n")
                print(f"  {bcolors.Vermelho}[*]{bcolors.Reset} Bloqueado\n")
                # print("TAM BLOQ",len(self.tabela_bloq))
                for i in self.tabela_bloq:
                    processo = list(filter(lambda x:x.pid == i,self.tabelaProcess))
                    process = processo[0]
                    print(f"  {bcolors.Branco}PID:{bcolors.Reset}",process.pid)
                    print(f"  {bcolors.Branco}PID parent:{bcolors.Reset}",process.paipid,end="")
                    print(f"\n  {bcolors.Branco}Tempo gasto:{bcolors.Reset}",process.tempo_cpu,end="")
                    print(f"\n  {bcolors.Branco}Instruções executadas:{bcolors.Reset}"," : ".join(list(map(lambda x:x.replace("\n",""), process.vetor_instrucoes))),end="")
                    print(f"\n  {bcolors.Branco}Memória:{bcolors.Reset}",process.vetor_memoria,end="")
                    print(f"\n  {bcolors.Branco}-----------{bcolors.Reset}")

                print(f"  {bcolors.Vermelho}-----------------------------------------------------------------------------------------------------------------------{bcolors.Reset}\n")
                print(f"  {bcolors.Verde}[*]{bcolors.Reset} Em Execução\n")
                # print("TAM BLOQ",len(self.tabela_bloq))
                for i in self.tabela_exec:
                    processo = list(filter(lambda x:x.pid == i,self.tabelaProcess))
                    process = processo[0]
                    print(f"  {bcolors.Branco}PID:{bcolors.Reset}",process.pid)
                    print(f"  {bcolors.Branco}PID parent:{bcolors.Reset}",process.paipid,end="")
                    print(f"\n  {bcolors.Branco}Tempo gasto:{bcolors.Reset}",process.tempo_cpu,end="")
                    print(f"\n  {bcolors.Branco}Instruções executadas:{bcolors.Reset}"," : ".join(list(map(lambda x:x.replace("\n",""), process.vetor_instrucoes))),end="")
                    print(f"\n  {bcolors.Branco}Memória:{bcolors.Reset}",process.vetor_memoria,end="")
                    print(f"\n  {bcolors.Branco}-----------{bcolors.Reset}")
                print(f"  {bcolors.Verde}-----------------------------------------------------------------------------------------------------------------------{bcolors.Reset}\n")



                # else:
                #     # parent

            elif (comando == "M"):
                print("  -----------")
                print(f"  {bcolors.Branco}[*]{bcolors.Reset} Processo Impressão Iniciado")
                print(f"\n\n  {bcolors.Amarelo}[*]{bcolors.Reset} Prontos\n")
                for i in self.tabela_pronto:
                    # print(self.tabela_pronto)
                    processo = list(filter(lambda x:x.pid == i,self.tabelaProcess))
                    process = processo[0]
                    print(f"  {bcolors.Branco}PID:{bcolors.Reset}",process.pid)
                    print(f"  {bcolors.Branco}PID parent:{bcolors.Reset}",process.paipid,end="")
                    print(f"\n  {bcolors.Branco}Tempo gasto:{bcolors.Reset}",process.tempo_cpu,end="")
                    print(f"\n  {bcolors.Branco}Instruções executadas:{bcolors.Reset}"," : ".join(list(map(lambda x:x.replace("\n",""), process.vetor_instrucoes))),end="")
                    print(f"\n  {bcolors.Branco}Memória:{bcolors.Reset}",process.vetor_memoria,end="")
                    print(f"\n  {bcolors.Branco}-----------{bcolors.Reset}")
                print(f"  {bcolors.Amarelo}-----------------------------------------------------------------------------------------------------------------------{bcolors.Reset}\n")

                print(f"  {bcolors.Vermelho}[*]{bcolors.Reset} Bloqueado\n")
                for i in self.tabela_bloq:
                    processo = list(filter(lambda x:x.pid == i,self.tabelaProcess))
                    process = processo[0]
                    print(f"  {bcolors.Branco}PID:{bcolors.Reset}",process.pid)
                    print(f"  {bcolors.Branco}PID parent:{bcolors.Reset}",process.paipid,end="")
                    print(f"\n  {bcolors.Branco}Tempo gasto:{bcolors.Reset}",process.tempo_cpu,end="")
                    print(f"\n  {bcolors.Branco}Instruções executadas:{bcolors.Reset}"," : ".join(list(map(lambda x:x.replace("\n",""), process.vetor_instrucoes))),end="")
                    print(f"\n  {bcolors.Branco}Memória:{bcolors.Reset}",process.vetor_memoria,end="")
                    print(f"\n  {bcolors.Branco}-----------{bcolors.Reset}")
                print(f"  {bcolors.Vermelho}-----------------------------------------------------------------------------------------------------------------------{bcolors.Reset}\n")

                print(f"  {bcolors.Verde}[*]{bcolors.Reset} Finalizados\n")
                for process in self.tabela_final:
                    print(f"  {bcolors.Branco}PID:{bcolors.Reset}",process.pid)
                    print(f"  {bcolors.Branco}PID parent:{bcolors.Reset}",process.paipid,end="")
                    print(f"\n  {bcolors.Branco}Tempo gasto:{bcolors.Reset}",process.tempo_cpu,end="")
                    print(f"\n  {bcolors.Branco}Instruções executadas:{bcolors.Reset}"," : ".join(list(map(lambda x:x.replace("\n",""), process.vetor_instrucoes))),end="")
                    print(f"\n  {bcolors.Branco}Memória:{bcolors.Reset}",process.vetor_memoria,end="")
                    print(f"\n  -----------")
                print(f"  {bcolors.Verde}-----------------------------------------------------------------------------------------------------------------------{bcolors.Reset}\n")

                # print(f"{bcolors.Verde}Warning: No active frommets remain. Continue?{bcolors.Reset}")







    def novo_processo(self, pid, paipid, pc, prioridade, estado, tempo_inicio, tempo_cpu, vetor_instrucoes, vetor_memoria):
        self.tabelaProcess.append(Processo_simulado(pid, paipid, pc, prioridade, estado, tempo_inicio, tempo_cpu, vetor_instrucoes, vetor_memoria, 0, 0.1))
        self.tabela_pronto.append(pid)
