import grpc
import helloworld_pb2_grpc
import helloworld_pb2

channel = grpc.insecure_channel('localhost:50051')
stub = helloworld_pb2_grpc.GreeterStub(channel)
response = stub.SayHello(helloworld_pb2.HelloRequest(name='Gaurav'))
print("Greeter client received: " + response.message)
response = stub.SayHelloAgain(helloworld_pb2.HelloRequest(name='Gauravv'))
print("Greeter client received: " + response.message)