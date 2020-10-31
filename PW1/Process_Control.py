import os  
def child():
   print('child Pid :',  os.getpid())
   os._exit(0)  

def parent(): 
    newpid = os.fork()
    if newpid == 0:  
        # if pid> 0 is parent
        print("call the child\n")
        child() 
        return newpid 
    elif newpid < 0: 
        print("Fork doesn't worked\n")
    else:
        pids = (os.getpid(), newpid) 
        child_pid = os.getpid()
        print("parent: %d, child: %d\n" % pids) 
        return child_pid 
     
r,w = os.pipe() 
  #funcao parente tambem pode criar um filho  


pid = parent()
print("Digite 1 para ler comandos de um arquivo\n 2 para digitar oscomandos") 
decision = int(input())   
if decision == 1:   
    pas_file = b" "
    #pid  = parent()
    f = open("Comandos.txt", "r") 
    line = f.readline()
    while line: 
        if line == "U": 
            pas_file = b"U"
        elif line == "L": 
            pas_file = b"L" 
        elif line == "I": 
            pas_file = b"I"  
        elif line == "M": 
            pas_file = b"M"  
        #assume-se que o processo controle é apenas pai
        if pid > 0: 
            # This is the parent process 
            # Closes file descriptor r 
                #os.close(r) 
            print("Parent process is writing") 
            text = pas_file 
            os.write(w, text) 
            print("Written text:", text.decode())  
        line = f.readline()  
        #pid  = parent()          
    f.close()      


if decision == 2:
    print("Digite um dos comando para o processo controle executar alguma operação:\nU: Fim de uma unidade de tempo.\n")
    print("L: Desbloqueia o primeiro processo simulado na fila bloqueada.\n")
    print("I: Imprime o estado atual do sistema.\n")
    print("M: Imprime o tempo médio do ciclo e finaliza o sistema.\n") 

    answer = str(input(""))
   # pid  = parent()
    while answer!= "M" : 
    
        if answer == "U": 
            pas = b"U"
        elif answer == "L": 
            pas = b"L" 
        elif answer == "I": 
            pas = b"I"  
        elif answer == "M": 
            pas = b"M"  
       #assume-se que o processo controle é apenas pai
        if pid > 0: 
		# This is the parent process 
		# Closes file descriptor r 
	        #os.close(r) 
	        print("Parent process is writing") 
	        text = pas 
	        os.write(w, text) 
	        print("Written text:", text.decode())            
        print("Digite um dos comando para o processo controle executar alguma operação:\n")
        answer = str(input(""))  
       # pid  = parent()