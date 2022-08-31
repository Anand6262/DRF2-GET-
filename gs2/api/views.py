import json
from django.shortcuts import render
from . models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
# Create your views here.


class student_details(APIView):
    def get(self, req, pk):
        if(req.method=='GET'):
            stu=Student.objects.get(id=pk)
            # def get(self, req, pk):
            # get(id=pk)
            # print(stu)
            serializer=StudentSerializer(stu)
            # print(serializer)
            # print(serializer.data)
            json_data=JSONRenderer().render(serializer.data)
            # print(json_data)
            return HttpResponse(json_data, content_type="application/json")
#We can also write student_details class like this-->
# class student_details(APIView):
#     def get(self, req, pk):
#         if(req.method=='GET'):
#             stu=Student.objects.get(id=pk)
#             serializer=StudentSerializer(stu)
#             return JsonResponse(serializer.data, safe=True)



#If we use this(return JsonResponse(serializer.data, safe=False)) to get all data we have to put safe= False
class student_list(APIView):
    def get(self, req):
        if(req.method=='GET'):
            stu=Student.objects.all()
            # def get(self, req, pk):
            # get(id=pk)
            # print(stu)
            serializer=StudentSerializer(stu, many=True)
            # print(serializer)
            # print(serializer.data)
            json_data=JSONRenderer().render(serializer.data)
            # print(json_data)
            return HttpResponse(json_data, content_type="application/json")