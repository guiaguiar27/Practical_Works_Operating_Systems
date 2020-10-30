# Python program to explain os.wait() method 

# importing os module 
import os 

# Create a child process 
# using os.fork() method 
pid = os.fork() 


# a Non-zero process id (pid) 
# indicates the parent process 
if pid : 
	
	# Wait for the completion of 
	# child process using 
	# os.wait() method	 
	status = os.wait() 
	print("\nIn parent process-") 
	print("Terminated child's process id:", status[0]) 
	print("Signal number that killed the child process:", status[1]) 

else : 
	print("In Child process-") 
	print("Process ID:", os.getpid()) 
	print("Hello ! Geeks") 
	print("Exiting") 
	

# using os.wait() method	 
# Parent process will wait till 
# the completion of child process 
# and then only it will 
# begin its execution 
