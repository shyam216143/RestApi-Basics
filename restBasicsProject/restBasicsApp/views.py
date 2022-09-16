import json
from django.shortcuts import render
from rest_framework.response import Response

from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView, ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView,RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin,UpdateModelMixin, DestroyModelMixin
from .serializers import Myserializer, Myserializer1
from rest_framework.status import *
from rest_framework import permissions
from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
# Create your views here.

from .models import *


@ api_view(['GET'])
def home(request):
    employee1 = student.objects.all()
    print(employee1)
    serializer = Myserializer1(employee1, many=True)
    # return Response({"status":200, "message":"hellon dude this is y rest project","payloadbjlkjb":serializer.data})
    return Response(serializer.data)


 
@ api_view(['POST'])
def post_home(request):
    employee1 = employee.objects.all()
    print(employee1)
    serializer = Myserializer(data=request.data)
    print("serializervis :",serializer)
    if serializer.is_valid():
        serializer.save()
   
    return Response(serializer.data)



@ api_view(['PUT'])
def update_home(request,id):
    employee1 = employee.objects.get(id=id)  
    print(employee1)
    serializer = Myserializer(instance=employee1, data=request.data)
    if serializer.is_valid():
        serializer.save()
   
    return Response(serializer.data)


@ api_view(['DELETE'])
def delete_home(request,id):
    employee1 = employee.objects.get(id=id)  
    print(employee1)
    employee1.delete()
    return Response("data has been deleted")


# mixins examples
class employeList(GenericAPIView, ListModelMixin):
    queryset= employee.objects.all()
    serializer_class = Myserializer
    def get(self,request):
        return self.list(request)


class employeCreate(GenericAPIView, CreateModelMixin):
    queryset= employee.objects.all()
    serializer_class = Myserializer
    def post(self,request):
        return self.create(request)



class employeRetrieve(GenericAPIView, RetrieveModelMixin):
    queryset= employee.objects.all()
    serializer_class = Myserializer
    def get(self,request, **kwargs):
        return self.retrieve(request, **kwargs)        






class employeUpdate(GenericAPIView, UpdateModelMixin):
    queryset= employee.objects.all()
    serializer_class = Myserializer
    def put(self,request, **kwargs):
        return self.update(request, **kwargs)        



class employeDestroy(GenericAPIView, DestroyModelMixin):
    queryset= employee.objects.all()
    serializer_class = Myserializer
    def delete(self,request, **kwargs):
        return self.destroy(request, **kwargs)                





class employeListAndCreate(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset= employee.objects.all()
    serializer_class = Myserializer
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)






class employeUpdateRetriveDestroy(GenericAPIView, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin):
    queryset= employee.objects.all()
    serializer_class = Myserializer
    def put(self,request, **kwargs):
        return self.update(request, **kwargs)   

    def get(self,request, **kwargs):
        return self.retrieve(request, **kwargs)      
    def delete(self,request, **kwargs):
        return self.destroy(request, **kwargs)                
      
         
#  concrete generic examples
class employeList1(ListAPIView):
    queryset=employee.objects.all()
    serializer_class = Myserializer


class employeCreate1(CreateAPIView):
    queryset=employee.objects.all()
    serializer_class = Myserializer    




class employeRetrieve1(RetrieveAPIView):
    queryset=employee.objects.all()
    serializer_class = Myserializer    


class employeUpdate1(UpdateAPIView):
    queryset=employee.objects.all()
    serializer_class = Myserializer    

class employeDestroy1(DestroyAPIView):
    queryset=employee.objects.all()
    serializer_class = Myserializer    


class employeListAndCreate1(ListCreateAPIView):
    queryset=employee.objects.all()
    serializer_class = Myserializer    


class employeRetrieveAndUpdate1(RetrieveUpdateAPIView):
    queryset=employee.objects.all()
    serializer_class = Myserializer    




class employeRetrieveAndDestroy1(RetrieveDestroyAPIView):
    queryset=employee.objects.all()
    serializer_class = Myserializer    





class employeRetrieveUpdateDestroy1(RetrieveUpdateDestroyAPIView):
    queryset=employee.objects.all()
    serializer_class = Myserializer    








# viewset

class employeeViewset(ViewSet):
    def list(self, request):
        queryset = employee.objects.all()
        serializer = Myserializer(queryset, many=True)
        return Response(serializer.data)
    def retrieve(self, request, pk):
        id = pk
        if id is not None:
            queryset = employee.objects.get(id = id)
            serializer = Myserializer(queryset)
            return Response({'serial':serializer.data,'msg':'successfully retrieved'})
    def update(self, request,pk=None):  
        id = pk
        queryset = employee.objects.get(id = id)
        serializer = Myserializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'update has done'})
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)    
    def destroy(self, request, pk):
        queryset = employee.objects.get(id=pk)
        queryset.delete()
        return Response({'message':"deleted successfully"})
    def create(self, request):
        serializer = Myserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'created single model instance successfully'})

        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)    



#  modelviewset

class employeeViewModelset(ModelViewSet):
    queryset = employee.objects.all()
    serializer_class= Myserializer
    # authentication_classes=[BasicAuthentication] # #his used for general login first
    # permission_classes=[IsAuthenticated]
    # authentication_classes=[SessionAuthentication]  # this used for session  login 
    # permission_classes=[IsAuthenticated]
    # permission_classes=[IsAdminUser] #this is used for permssion for only admin user

from rest_framework.renderers import JSONRenderer, StaticHTMLRenderer
class employeeViewModelset1(ModelViewSet):
    queryset = employee.objects.all()
    serializer_class= Myserializer1
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

   
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


from django.http import HttpResponse
def example(request, pk):
    x = employee.objects.get(id=pk)
    print("model object is ",x)
    print("type of model object is ",type(x))
    serial = Myserializer(x)
    print("total serializer is :",serial)
    print("total serializer type is :",type(serial))
    print("data  is ",serial.data)
    print("type of data is ",type(serial.data))
    json_data = JSONRenderer().render(serial.data)
    print("json  data  is ",json_data)
    print("type of json data is ",type(json_data))
    return HttpResponse(json_data, content_type='application/json')

import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser
@csrf_exempt
def example1(request):
    if request.method == 'POST':
        json_data = request.body
        print(json_data)
        stream = io.BytesIO (json_data)
        print(stream)
        python_data = JSONParser().parse(stream)
        print(python_data)
        serializer = Myserializer(data=python_data)
        print(serializer)
        if serializer.is_valid() :
            print("hello")
            serializer.save()
            print("hello1")
            res={"msg":"successfully created"}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
       
        json_data = JSONRenderer().render(serializer.errors)    
        return HttpResponse(json_data, content_type='application/json')

import io
from .serializers import ExampleSerializer
@csrf_exempt
def example2(request):
    if request.method=='GET':
        json_data= request.body
        print("data is:",json_data)
        stream = io.BytesIO(json_data)
        print(stream)
        python_data = JSONParser().parse(stream)
        print(python_data)
        id = python_data.get('id', None)
        print(id)
        if id is not None:
            emp = employee.objects.get(id = id)
            print(emp)
            serializer = Myserializer(emp)
            print(serializer.data)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')
        emp = employee.objects.all()  
        serializer = Myserializer(emp, many=True)
        json_data = JSONRenderer().render(serializer.data)  
        return HttpResponse(json_data, content_type='application/json')  



    if request.method=='POST':      
        json_data= request.body
        print("data is:",json_data)
        stream = io.BytesIO(json_data)
        print(stream)
        python_data = JSONParser().parse(stream)
        print(python_data)
        serializer = Myserializer(data=python_data)
        print(serializer)
        if serializer.is_valid() :
            serializer.save()
            res={"msg":"successfully created"}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
       
        json_data = JSONRenderer().render(serializer.errors)    
        return HttpResponse(json_data, content_type='application/json')