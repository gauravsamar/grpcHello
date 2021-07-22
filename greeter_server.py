import grpc
from concurrent import futures
import logging
import helloworld_pb2
import helloworld_pb2_grpc
class Greeter(helloworld_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return helloworld_pb2.HelloReply(message='Hello, %s!' % request.name)
    def SayHelloAgain(self, request, context):
        return helloworld_pb2.HelloReply(message='Hello again, %s!' % request.name)


server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(),server)
print('Starting server. Listening on port 50051')
server.add_insecure_port('[::]:50051')
server.start()
server.wait_for_termination()
