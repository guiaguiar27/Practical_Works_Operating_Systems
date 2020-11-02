class Processos: 
    def __init__(self): 
        self.vetor_instrucoes = [] 
        self.tam = 0  
        self.id = 0 
#preenche os processos com um campo destinado ao tamanho das instrucoes    
def fill_size(Processos): 
    for nr in Processos:
        nr.tam = len(nr.vetor_instrucoes)
    return Processos 
#quiqck sort 
def partition_Short(process, low, high):
    i = (low-1)         # index of smaller element
    pivot = process[high].tam     # pivot
    for j in range(low, high):
        if process[j].tam <= pivot:
            i = i+1
            process[i].tam, process[j].tam  = process[j].tam , process[i].tam
 
    process[i+1].tam , process[high].tam  = process[high].tam , process[i+1].tam
    return (i+1)
def quickSort_Short(process, low, high):
    if len(process) == 1:
        return process
    if low < high:
        pi = partition_Short(process, low, high)
        quickSort_Short(process, low, pi-1)
        quickSort_Short(process, pi+1, high)  

def Shortest_job_First(Processos):   
    fill_size(Processos) 
    size = len(Processos)   
    quickSort_Short(Processos,0,size-1)  
    Processos.reverse()
    return Processos
 



# vec = ['l','u','teste'] 
# vec2 = ["j", "k"] 
# vec3 = ["j", "k", "a","b","z"] 
# vec4 = ["l"]
# process = []
# for i in range(4):  
#     process.append(Processos()) 
# count = 3   
# for i in process:  
#     if count == 2 : 
#         i.vetor_instrucoes = vec   
#         i.id = 2
#     elif count == 1 :  
#         i.vetor_instrucoes = vec2 
#         i.id = 1 
#     elif count == 3 :  
#         i.vetor_instrucoes = vec3  
#         i.id = 3 
#     elif count == 0: 
#         i.id = 0 
#         i.vetor_instrucoes = vec4
#     count -=1   

# for i in process: 
#     print(i.vetor_instrucoes[:]) 
# 
# 
# 
# 
#  
#                       ATENCAOOO 
#usa  na funcao pra chamar o escalonamento  
Shortest_job_First(process) 
print("quicksort") 
for i in process: 
    print(i.vetor_instrucoes[:]) 

while process != []: 
    print("Processo Para executar:",process[0].id)
    #importante colocar na funcao para reogarnizar a lista  
    #sempre o processo na posicao zero que sera executado
    process.pop(0) 
    for i in process:  
        print(i.vetor_instrucoes[:]) 
    
