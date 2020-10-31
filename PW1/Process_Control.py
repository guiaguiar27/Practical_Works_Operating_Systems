import os  


  #funcao parente tambem pode criar um filho  

r,w = os.pipe() 

print("Digite 1 para ler comandos de um arquivo\n 2 para digitar oscomandos") 
decision = int(input())   

if decision == 1:    
    pid = os.fork()
       #assume-se que o processo controle é apenas pai
    pas_file = b" "
    if pid > 0:  
        os.close(r) 
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
         
            print("Parent process is writing") 
            text = pas_file 
            os.write(w, text) 
            print("Written text:", text.decode()) 
            line = f.readline()  
        f.close()
    if pid == 0:
        os.close(w)
        print("Child esta lendo...")
        print("PID filho: ",os.getpid())
        r = os.fdopen(r)
        text = r.read()
        print("Texto lido: ",text)            
        # pid  = parent()


if decision == 2:    
    pid = os.fork()
       #assume-se que o processo controle é apenas pai
    pas = b" "
    if pid > 0:  
        os.close(r)  
        print("Digite um dos comando para o processo controle executar alguma operação:\nU: Fim de uma unidade de tempo.\n")
        print("L: Desbloqueia o primeiro processo simulado na fila bloqueada.\n")
        print("I: Imprime o estado atual do sistema.\n")
        print("M: Imprime o tempo médio do ciclo e finaliza o sistema.\n") 
        answer = str(input(""))   
        while answer != "M":     
            if answer == "U": 
                pas = b"U"
            elif answer == "L": 
                pas = b"L" 
            elif answer == "I": 
                pas = b"I"  
            elif answer == "M": 
                pas = b"M"    
            text = pas 
            os.write(w, pas)  
            print("Parent process is writing") 
            print("Written text:", text.decode()) 
            print("Digite um dos comando para o processo controle executar alguma operação:\n")
            answer = str(input(""))  

           
    if pid == 0:
        os.close(w)
        print("Child esta lendo...")
        print("PID filho: ",os.getpid())
        r = os.fdopen(r)
        text = r.read()
        print("Texto lido: ",text)