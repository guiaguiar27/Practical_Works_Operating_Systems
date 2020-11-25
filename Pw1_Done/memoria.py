class var_Memoria:

    def __init__(self):
        self.ocupado = False
        self.pid = 0.1

def print_memory(memory):
    for i in range(len(memory)):
        if memory[i].ocupado == True:
            print("Faixa ocupada - PID {} - Variavel {}".format(memory[i].pid, memory[j].variavel ))


# def aloca_mem_processo_NF(memory, num_var, pid, last_position):
#     for i in range(last_position, size(memory)):
#         count = 0
#         for j in range(i, num_var + 1):
#             if (memory[j].ocupado == False):
#                 count += 1
#             else:
#                 break
#         if (count == num_var):
#             for j in range(j,num_var + 1):
#                 pid = pid
#                 ocupado = True
#              return True
#         if i == size(memory) :
#             return False


def aloca_mem_processo_FF(memory, num_var, pid):
    # cada segmento comporta apenas 1 memória
    print("O processo que ta tentando alocar é:", pid)
    for k in range(len(memory)):
        print("Ta ocupado", k, memory[k].ocupado)
    for i in range(len(memory)):
        count = 0
        if ((i + num_var) <= len(memory)):

            for j in range(i, i + num_var):
                if (memory[j].ocupado == False):
                    count += 1
                else:
                    break
            if (count == num_var):
                for j in range(i, i + num_var ):
                    print("Num var inserir:", num_var)
                    print("Pos inserir:", j)
                    memory[j].pid = pid
                    memory[j].ocupado = True
                return True
        else:
            print("Retornou falso")
            return False

def desaloca_mem_processo(memory, num_var, pid):
    count = 0
    print("Processo que ta desalocando:", pid)
    for i in range(len(memory)):
        if(memory[i].pid == pid):
            memory[i].pid = 0.1
            memory[i].ocupado = False
            count += 1
            print("Num var remover:", num_var)
            print("Pos remover:", i)
        if(count == num_var):
            return
