class Processo_simulado:
    def __init__(self):
        self.vetor_memoria = []
        self.pc = 0
        self.contador = [] #essa variavel garante que a posição da memória foi alocada e que também teve um valor atribuido a ela


    def ler_arquivo_init(self, nome_arquivo, pc_inicial):
        with open(nome_arquivo, "r") as f:
            count_bloq = 0
            for line in f:
                count_bloq+=1

                if count_bloq < pc_inicial+1: #garante que o programa volte a executar a partir da instrução que parou
                    break

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
                    #na hora que voltar tem que voltar com o nome do arquivo que tava executando e o contador de processos que terminou
                    #então tem que ter alguma coisa do tipo: return (nome_arquivo, self.pc)
                elif line[0] == 'T':
                    print("Termina processo")
                    #matar o processo
                elif line[0] == 'F':
                    processo = Processo_simulado()
                    processo.ler_arquivo_init()
                elif line[0] == 'R':
                    self.pc = 0
                    self.ler_arquivo_init(line[1])
                else:
                    print("Arquivo com comando inválido")
                    break
        print(self.vetor_memoria)


a = Processo_simulado() 
a.ler_arquivo_init("teste_processo.txt", 0)