import xmlrpc.client
import time

# Conectar ao servidor
server = xmlrpc.client.ServerProxy('http://localhost:8000', allow_none=True)

class ComplexType:
    def __init__(self, number, string):
        self.number = number
        self.string = string

# Função para medir o tempo de execução
def timed_operation(func, *args):
    start_time = time.perf_counter()
    result = func(*args)
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    return result, elapsed_time

# Chamar funções remotas e imprimir os resultados e tempo de execução
def perform_operation(operation, *args):
    result, elapsed_time = timed_operation(operation, *args)
    print(f"Operation result: {result} (Time taken: {elapsed_time:.9f} seconds)")

# Chamar as funções remotas com temporizadores
print("Calling remote operations with timers:")
result, elapsed_time = timed_operation(server.void)
print(f"Void operation completed in {elapsed_time:.9f} seconds")
perform_operation(server.long_function, 100000000)
perform_operation(server.multiple_long_function, 100000000, 100000000, 100000000, 100000000, 100000000, 100000000, 100000000, 100000000)
perform_operation(server.string_operation, "hello world")
complex_value = ComplexType(1, "matheus")
perform_operation(server.complex_operation, complex_value)
perform_operation(server.multiple_string, "hello", "world", "helloworld", "helloworld", "helloworld", "helloworld")