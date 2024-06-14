from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

class ComplexType:
    def __init__(self, number, string):
        self.number = number
        self.string = string

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Criar o servidor
server = SimpleXMLRPCServer(("localhost", 8000), requestHandler=RequestHandler, allow_none=True)
server.register_introspection_functions()

# Funções para serem expostas
def void():
    return

def long_function(a):
    return a

def multiple_long_function(a, b, c, d, e, f, g, h):
    return a + b + c + d + e + f + g + h

def string_operation(value):
    return value[::-1]

def complex_operation(complex_value):
    return ComplexType(complex_value["number"] + 1, complex_value["string"])

def multiple_string(s1, s2, s3, s4, s5, s6):
    return s1 + s2 + s3 + s4 + s5 + s6

# Registrar funções
server.register_function(void, 'void')
server.register_function(long_function, 'long_function')
server.register_function(multiple_long_function, 'multiple_long_function')
server.register_function(string_operation, 'string_operation')
server.register_function(complex_operation, 'complex_operation')
server.register_function(multiple_string, 'multiple_string')

# Executar o servidor
print("Server is running on port 8000...")
server.serve_forever()
