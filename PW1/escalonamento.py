import time 

def partition(process, low, high):
    i = (low-1)         # index of smaller element
    pivot = process[high].prioridade     # pivot
    for j in range(low, high):
        if process[j].prioridade <= pivot:
            i = i+1
            process[i].prioridade, process[j].prioridade = process[j].prioridade, process[i].prioridade
 
    process[i+1].prioridade, process[high].prioridade = process[high].prioridade, process[i+1].prioridade
    return (i+1)
def quickSort(process, low, high):
    if len(process) == 1:
        return process
    if low < high:
        pi = partition(process, low, high)
        quickSort(process, low, pi-1)
        quickSort(process, pi+1, high)
def initilize(processos): 
    for i in processos:     
        i.requisite = 0 
    return processos    


def escalonamento(processos):  
    n = len(processos) 
    quickSort(processos, 0, n-1)
    quantum = 1.0   
    for i in processos: 
        if i.prioridade == 0 :   
            i.quantum = quantum  
            if i.requisite == 1 : # o processo usou todo seu quantum para executar   
                i.prioridade = 1 #prioridade diminuida 
                   
        elif i.prioridade == 1:   
            i.quantum = 2*quantum  
            if i.requisite == 1 : # o processo usou todo seu quantum para executar  
                i.prioridade = 2 #prioridade diminuida 
                
            if i.estado == 1: 
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
            if i.requisite == 1: 
                i.quantum = 16*quantum  
        # for i in fila:    
        #         for j in processos: 
        #             if i.prioridade == j.prioridade: 
        #                 i.processo = deque(j)
                
    initilize(processos)
    return processos  


process = [] 
lista_processos = [] 
# count = 0 
# aux = 0.0   
# print("Marcador")
# for i in range(10): 
#     id = int(input(" id : "))  
#     process.append(Processos(count,0.0,1, id)) 
#     count +=1     
#     if count > 3: 
#         count = 0
# # count = 0     
# # for i in process:   
# #     print("Processo {}: {}" .format(count+1, i.prioridade)) 
# #     count+=1 
# # fifo  = escalonamento(process)   
# # print("escalonamento") 
# # count = 0   
# # for i in process:   
# #     print("Processo {}: {}" .format(count+1, i.prioridade)) 
# #     count+=1 


# count = 0  

# for i in process:  
#         print("Processo {}: {}" .format(i.id, i.prioridade))
# i.tempoCpu = aux      

# while count < 4:  
#     #escalona a lista  
#     #deve ser utilizada junto ao escalonamento
#     lista_processos = escalonamento(process)   
#     print("escalonamento ")
    
#     for i in lista_processos:  
#         print("Processo {}: {}" .format(i.id, i.prioridade))
#     #zera os tempos de uso de cpu  
#     #deve ser utilizada junto ao escalonamento
      
#     #imprime o tempo de cpu antes da execução    
#     for i in lista_processos: 
#         print("Processo {}: {}" .format(i.id, i.tempoCpu))

   
   
#     #percoore os processos  
#     #execucao  
#     for i in lista_processos:   
#         print(i.id)
#         if i.prioridade == 3:  
#             i.tempoCpu += 2.0  
#             print("Tempo {} processo{}".format(i.tempoCpu, i.id))          
#         if i.tempoCpu == i.quantum: 
#             i.requisite = 1   

        
#     #     if i.prioridade%2 == 0 : 
#     #          i.tempoCpu += 0.5 
#     #     else :  
#     #         i.tempoCpu += 0.5
       
#     # # assinala se for bloqueado 
#     #     if i.prioridade == 2 or i.prioridade == 3 or i.prioridade == 1: 
#     #         i.blocked = 1
#     #         i.tempoCpu +=8 




#     #mostra tempo de cpu dps da execucao 
#     print("Lista de processo")         
#     for i in lista_processos:  
#         print("PID {}: tempoCpu:{},Prioridade:{} " .format(i.id, i.tempoCpu,i.prioridade))  

#     #copia a lista modificada para a lista que será escalonada
#     #deve ser utilizada junto ao escalonamento
#     procces = lista_processos.copy()  
#     print("lista de processos que sera escalonada")
#     for i in process:  
#         print("PID {}: tempoCpu:{},Prioridade:{} " .format(i.id, i.tempoCpu,i.prioridade))  

#     count += 1     