import socket
import threading
from queue import Queue
from sniffer import *

number_of_threads = 2          #because we need 2 threads for 2 jobs to be done listnening and speaking
job_number = [1, 2]              #first and second thread
queue = Queue()
all_connections = []            #all the connection objects
all_address = []                #all ips addresse and ports

#socket creation
def building_socket():
    try:        #(try) to avoid any error in socket creation(some times it happen)
        global host         # globalised the variables so they can be accessed outside the function
        global port_number
        global sock
        host = ""  # THE IP address of the server should be added here
        port_number = 6666
        sock = socket.socket()   # function used to create socket
    except socket.error as msg:  # the error will be stored as message and it will be converted to str
        print("Error in creating the socket: " + str(msg))

#socket binding to the port
def socket_binding():
    try:
        global host
        global port_number
        global sock

        sock.bind((host, port_number))    #binding the socket with the host and port(the variables will be retreived as they are globalized)
        sock.listen(5)                  #maximm number is 5

    except socket.error as msg:
        print("Error in binding the socket" + str(msg))
        socket_binding()                #recursion technique to call the bind socket again

#accepting connections from multible clients
def accepting_connection():
    for i in all_connections:
        i.close()
    del all_connections[:]          # deleting all the data the list contain for a new start
    del all_address[:]
    while True:
        try:

            conn, addr = sock.accept()      #accepting the connection will return ip address and port numebr(stored in addr),the connection object will be stored in conn.
            sock.setblocking(1)             #prevent time-out
            all_connections.append(conn)    #
            all_address.append(addr)        #
            print("connection is established " + "IP = " + addr[0] + "Port = " + str(addr[1]))   # port number is int, need to be str
        except:
            print("Error")


#creating workers for multithreading
def workers_creation():
    for i in range(number_of_threads):        #loop for the number of threads which are 2
        t = threading.Thread(target=work)     #variable t contain the thread created and passed the parameter required
        t.demon = True                     #make sure that when the program ends the thread also ends
        t.start()                 #starting the thread

#doing next job in the queue
def work():
    x = queue.get()
    if x == 1:
        building_socket()
        socket_binding()
        accepting_connection()
    if x == 2:
        sniffer()

    queue.task_done()

#creating the job queue and joining it
def create_job():
    for i in job_number:    #loop on the number of jobs
        queue.put(i)

    queue.join()

workers_creation()
create_job()

