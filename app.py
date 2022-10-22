from wsgiref.simple_server import make_server  
from pyramid.config import Configurator  
from pyramid.response import Response  
  
def helloWorld(request):  
    return Response('<h1>Hello, World! Welcome to Javatpoint.com</h1>')  
  
if __name__ == '__main__':  
    with Configurator() as cnfg:  
        cnfg.add_route('hello', '/')  
        cnfg.add_view(helloWorld, route_name = 'hello')  
        myApp = cnfg.make_wsgi_app()  
    myServer = make_server('0.0.0.0', 8000, myApp)  
    myServer.serve_forever()