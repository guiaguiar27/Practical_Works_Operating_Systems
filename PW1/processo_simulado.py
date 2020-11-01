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
            aux = self.executa_funcao()
            while aux[0] == 'N' | aux[0] == 'D' | aux[0] =='V': #substitui os valores da memoria atuais pelos valores presentes no novo arquivo
                self.executa_funcao()
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
       

    def troca_de_contexto(self, pid_novo):
        self.insere_processo_cpu(pid_novo)

    def le_entrada(self, comando):
            comando = self.text[0]
            if (comando == "U"):
                aux = self.cpu.executa_funcao()
                if aux[0] == 'B':
                    estado = 1
                    self.novos_valores_processo(estado)
                    self.tabela_bloq.append(self.cpu.pid)
                    self.tabela_exec.remove(self.cpu.pid)
                    #ESCALONAMENTO É FEITO NO FINAL
                elif aux[0] == 'T':
                    self.tabela_exec.remove(self.cpu.pid)
                    for i in self.tabelaProcess:
                        if i.pid == self.cpu.pid:
                            self.tabelaProcess.remove(i)
                     #O NOVO PID É O PROXIMO PROCESSO A SER EXECUTADO NA LISTA DE PRONTOS
                     #ESCALONAMENTO É FEITO NO FINAL
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

                    # if self.cpu.tempo_cpu == self.cpu.quantum_processo: SE ISSO AQUI FOR TRUE O PROCESSO TEM QUE IR PRA PARTE DE PRONTO E PARAR DE EXECUTAR
                    #     for i in self.tabelaProcess:
                    #         if i == self.cpu.pid:
                    #             i.requisite = 1
                    # novo_pid = self.tabela_pronto[0]
                    #     for i in self.tabelaProcess:
                    #         if i.pid == novo_pid:
                    #             i.estado = 2
                    #     self.insere_processo_cpu(novo_pid)
                    #     self.tabela_exec.append(novo_pid)
                    #     self.tabela_pronto.remove(novo_pid)


    def novo_processo(self, pid, paipid, pc, prioridade, estado, tempo_inicio, tempo_cpu, vetor_instrucoes, vetor_memoria):
        self.tabelaProcess.append(Processo_simulado(pid, paipid, pc, prioridade, estado, tempo_inicio, tempo_cpu, vetor_instrucoes, vetor_memoria, 0, 0.1))
        self.tabela_pronto.append(pid)      


gerenciador = Gerenciador()
for i in  range(18):
    gerenciador.le_entrada('U')
print("Tempo final do gerenciado", gerenciador.tempo_atual)