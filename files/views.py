from django.shortcuts import render
from rest_framework import generics
from django.conf import settings
from .models import Files
import os
from rest_framework.views import APIView, Request, Response, status
from .serializers import UpFileSerializer, FilesSerializer


class FileView(APIView):
    def post(self, request: Request):
        with open("uploads/upFiles/CNAB.txt", "r") as line:
            lines = line.readlines()
        for i in lines:
            typeOf = i[0]
            dataPt3 = i[1:5]
            dataPt2 = i[5:7]
            dataPt1 = i[7:9]
            value = int(i[9:19]) / 100
            cpf = i[19:30]
            card = i[30:42]
            time = i[42:48]
            owner = i[48:62]
            store = i[62:81]

            infos = {
                "typeOf": typeOf,
                "data": dataPt1 + "/" + dataPt2 + "/" + dataPt3,
                "value": value,
                "cpf": cpf,
                "card": card,
                "time": time,
                "owner": owner,
                "store": store,
            }
            serializer = FilesSerializer(data=infos)
            serializer.is_valid(raise_exception=True)

            serializer.save()
        lists = Files.objects.all()
        serializer = FilesSerializer(lists, many=True)
        os.remove("uploads/upFiles/CNAB.txt")
        return Response(serializer.data, status.HTTP_201_CREATED)

    def get(self, request: Request):
        lists = Files.objects.all()
        serializer = FilesSerializer(lists, many=True)
        return Response(serializer.data)


class UpFile(generics.CreateAPIView):
    serializer_class = UpFileSerializer
