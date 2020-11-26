class var_Memoria:

    def __init__(self):
        self.ocupado = False
        self.pid = 0.1


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


def aloca_mem_processo_FF(memory, num_var, pid, mem_virtual):
    # cada segmento comporta apenas 1 memória
    #print("#################################################O processo que ta tentando alocar é:", pid)
    andou_virtual = 0 #numero de espaços que teve que percorrer para alocar no vetor da memoria virtual
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
                    memory[j].pid = pid
                    memory[j].ocupado = True
                return True, i 
        else:
            andou_virtual = aloca_mem_virtual(mem_virtual, num_var, pid)
            #print("Retornou falso")
            return True, (len(memory) + andou_virtual) 

def desaloca_mem_processo(memory, num_var, pid, mem_virtual):
    count = 0
    num_fragmentos_livres = 0
    desalocou = False
    #print("################################################Processo que ta desalocando:", pid)
    for i in range(len(memory)):
        if(memory[i].pid == pid):
            memory[i].pid = 0.1
            memory[i].ocupado = False
            count += 1
            desalocou = True
        if(memory[i].ocupado == False):
            num_fragmentos_livres += 1
    
    if desalocou == False:
        desaloca_mem_virtual(mem_virtual, num_var, pid)
        return 0 #como a desalocação não foi feita na memoria principal, o numero de fragmentos externos nela permanece constante
        #mas ainda assim houve uma desalocação, então continua precisando contar isso para a media de fragmentos externos
    #print("Num fragmentos livres 1:", num_fragmentos_livres)
    return num_fragmentos_livres
           
def aloca_mem_virtual(mem_virtual, num_var, pid):
    tam_mem_virt = len(mem_virtual)
    for i in range(num_var):
        alocar = var_Memoria()
        alocar.pid = pid
        alocar.ocupado = True
        mem_virtual.append(alocar)
    return(tam_mem_virt)

def desaloca_mem_virtual(mem_virtual, num_var, pid):
    #print("Tamanho mem virtual", len(mem_virtual))
    count = 0
    while count < num_var:
        for i in mem_virtual:
            if(i.pid == pid):
                mem_virtual.remove(i)
                count += 1
                #print("Removeu")
            