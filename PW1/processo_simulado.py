import threading
import time
class Processo_simulado:
    def __init__(self, pc_inicial):
        self.vetor_memoria = []
        self.pc = pc_inicial
        self.contador = [] #essa variavel garante que a posição da memória foi alocada e que também teve um valor atribuido a ela

    def copia_dados(self, vetor, pc, contador):
        self.vetor_memoria = vetor.copy()
        self.pc = pc
        self.contador = contador.copy()
        
    def ler_arquivo_init(self, nome_arquivo):
        with open(nome_arquivo, "r") as f:
            count_bloq = 0
            for line in f:
                count_bloq+=1
                if count_bloq < self.pc + 1: #garante que o programa volte a executar a partir da instrução que parou
                    continue
                else:
                    self.pc+=1
                    line = line.split()
                    if line[0] == 'N':
                        self.vetor_memoria = [0 for x in range(int(line[1]))]
                        self.contador = [0 for x in range(int(line[1]))]
                    elif line[0] == 'D':
                        self.contador[int(line[1])] += 1
                        continue
                    elif line[0] == 'V':
                        index = int(line[1])
                        self.vetor_memoria[index] = int(line[2])
                        self.contador[int(line[1])] += 1
                    elif line[0] == 'A':
                        index = int(line[1])
                        if self.contador[index] == 2:
                            self.vetor_memoria[index] = self.vetor_memoria[index] + int(line[2])
                        else:
                            print("Posição ainda não possui valor inicial, ou não foi alocada")  
                            break 
                    elif line[0] == 'S':
                        index = int(line[1])
                        if self.contador[index] == 2:
                            self.vetor_memoria[index] = self.vetor_memoria[index] - int(line[2])
                        else:
                            print("Posição ainda não possui valor inicial, ou não foi alocada")  
                            break   
                    elif line[0] == 'B':
                        print("Bloqueia processo")
                        #manda o pc pra tabela processos
                        #na hora que voltar tem que voltar com o nome do arquivo que tava executando, o contador de processos que terminou e o estado atual 
                        #do vetor de dados
                        #então tem que ter alguma coisa do tipo: return (nome_arquivo, self.pc)
                    elif line[0] == 'T':
                        print(self.vetor_memoria)
                        print("Termina processo")
                        break
                        #matar o processo
                    elif line[0] == 'F':
                        vec_aux = self.vetor_memoria                   
                        processo = Processo_simulado(0)                       
                        processo.copia_dados(self.vetor_memoria, self.pc, self.contador)                        
                        thread = threading.Thread(target=processo.ler_arquivo_init,args=(nome_arquivo,))
                        thread.start()                        
                        #time.sleep(0.1)
                        self.vetor_memoria = vec_aux              
                        index = int(line[1])                   
                        count_bloq = self.pc
                        self.pc = self.pc + index #avança x instruções e começa a executar a partir delas
                    elif line[0] == 'R':
                        self.pc = 0
                        self.ler_arquivo_init(line[1])
                    else:
                        print("Arquivo com comando inválido")
                        break


a = Processo_simulado(0) 
a.ler_arquivo_init("teste_processo.txt")