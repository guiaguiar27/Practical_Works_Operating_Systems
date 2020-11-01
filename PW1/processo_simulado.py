import threading
import time
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
            print("Bloqueia processo")
            self.pc = self.pc + 1
        elif line[0] == 'T':
            self.pc = self.pc + 1
            print("Termina processo", self.vetor_memoria)
        elif line[0] == 'F':
            print("Cria novo processo")                 
        elif line[0] == 'R':
            self.pc = 0
            self.vetor_instrucoes = self.le_instrucoes(line[1]) #substitui as instruções atuais pelas instruções no novo arquivo
        else:
            print("Arquivo com comando inválido")
            exit
        self.tempo_cpu += 1
        return(line)
    
    def retorna_valores(self):
        return( self.vetor_instrucoes, self.vetor_memoria, self.pc, self.tempo_cpu)



class Gerenciador:
    def __init__(self):
        self.tabelaProcess = []
        self.tabela_pronto = []
        self.tabela_bloq = []
        self.tabela_exec = []
        self.text = "U"
        self.tempo_atual = 0
        self.cpu = Cpu(0 ,0, 0, 0, 0, 1)
        self.newProcess_0('teste_processo.txt')
        self.processo_escalonado = 0

    def newProcess_0(self, nome_arquivo):
        vetor_instrucoes = self.cpu.le_instrucoes(nome_arquivo)
        processo = Processo_simulado(0, 0, 0, 2, 0, 0, 0, vetor_instrucoes, [], 0, 0.1)
        self.tabelaProcess.append(processo)
        self.tabela_exec.append(0)
        self.insere_processo_cpu(processo.pid)

    def insere_processo_cpu(self, pid):
        for i in self.tabelaProcess:
            if i.pid == pid:
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
        if self.tabela_pronto != []:
            processos = self.tabelaProcess.copy()
            processos = self.escalonamento(processos)
            for i in processos:
                if i.estado == 0:
                    self.tabela_exec.append(i.pid)
                    self.insere_processo_cpu(i.pid)
                    self.tabela_pronto.remove(i.pid)
                    break
        else:
            print("Não existem mais processos no estado pronto") 
            self.cpu = None
    def le_entrada(self, comando):
            comando = self.text[0]
            if (comando == "U"):
                aux = self.cpu.executa_funcao()
                if aux[0] == 'B':
                    estado = 1
                    print(self.tabela_pronto)
                    self.novos_valores_processo(estado)
                    self.tabela_bloq.append(self.cpu.pid)
                    self.tabela_exec.remove(self.cpu.pid)
                    #ESCALONAMENTO É FEITO NO FINAL
                    self.troca_contexto()
                elif aux[0] == 'T':
                    self.tabela_exec.remove(self.cpu.pid)
                    for i in self.tabelaProcess:
                        if i.pid == self.cpu.pid:
                            self.tabelaProcess.remove(i)
                    
                     #O NOVO PID É O PROXIMO PROCESSO A SER EXECUTADO NA LISTA DE PRONTOS
                     #ESCALONAMENTO É FEITO NO FINAL
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

                if self.cpu.tempo_cpu == self.cpu.quantum_processo: #SE ISSO AQUI FOR TRUE O PROCESSO TEM QUE IR PRA PARTE DE PRONTO E PARAR DE EXECUTAR
                    for i in self.tabelaProcess:
                        if i == self.cpu.pid:
                            i.requisite = 1
                            self.novos_valores_processo(0)
                            self.tabela_pronto.append(self.cpu.pid)
                            self.tabela_exec.remove(self.cpu.pid)
                            self.troca_contexto()
                            break


    def novo_processo(self, pid, paipid, pc, prioridade, estado, tempo_inicio, tempo_cpu, vetor_instrucoes, vetor_memoria):
        self.tabelaProcess.append(Processo_simulado(pid, paipid, pc, prioridade, estado, tempo_inicio, tempo_cpu, vetor_instrucoes, vetor_memoria, 0, 0.1))
        self.tabela_pronto.append(pid)      


gerenciador = Gerenciador()
for i in  range(18):
    gerenciador.le_entrada('U')
print("Tempo final do gerenciado", gerenciador.tempo_atual)