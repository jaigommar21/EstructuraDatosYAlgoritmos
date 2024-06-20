
import threading
import time


from  QueueSimpleArray import QueueSimpleArray


class Client:

    def __init__(self,name ):
        self.name = name

    def __str__(self):
        return f"Cliente {self.name}"

class Server(threading.Thread):

    def __init__(self, queue_clients):
        super().__init__()
        self.queue_clients = queue_clients

    def run(self):
        while True:
            #print("Atendiendo ...!")
            time.sleep(1) # Es necesario si no no funciona el servidor
            if  not self.queue_clients.isEmpty():
                cliente = self.queue_clients.deQueue()
                #print(type(cliente))
                print(f"{cliente.name} está siendo atendido.")
                #time.sleep(1)  # Simulación de tiempo de atención
            else:
                break

#################################
# Main
#################################
if __name__ == '__main__':
    
    cola_clientes = QueueSimpleArray(10)
    server = Server(cola_clientes)
    server.start()

    clientes = ["Jaime","Juan","Eduardo","Pedro","Moises","Maria","Sara","Marco","Susana"]
    for name in clientes:
       
        cliente = Client(name)
        cola_clientes.enQueue(cliente)
        print(f"Cliente {cliente.name} acaba de llegar ...!")


    server.join()
    print("Todos los clientes han sido atendidos.")




