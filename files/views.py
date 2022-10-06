from django.shortcuts import render
from rest_framework import generics
from django.conf import settings
from .models import Files
from rest_framework.views import APIView, Request, Response, status
from .serializers import UpFileSerializer, FilesSerializer


class FileView(APIView):
    def post(self, request: Request):
        with open("uploads/upFiles/CNAB.txt", "r") as line:
            lines = line.readlines()
        for i in lines:
            print(i)
            tipo = i[0]
            dataPt3 = i[1:5]
            dataPt2 = i[5:7]
            dataPt1 = i[7:9]
            valor = int(i[9:19]) / 100
            cpf = i[19:30]
            cartao = i[30:42]
            hora = i[42:48]
            dono_da_loja = i[48:62]
            nome_loja = i[62:81]

            infos = {
                "tipo": tipo,
                "data": dataPt1 + "/" + dataPt2 + "/" + dataPt3,
                "valor": valor,
                "cpf": cpf,
                "cartao": cartao,
                "hora": hora,
                "dono_da_loja": dono_da_loja,
                "nome_loja": nome_loja,
            }
            serializer = FilesSerializer(data=infos)
            serializer.is_valid(raise_exception=True)

            serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)

    def get(self, request: Request):
        lists = Files.objects.all()
        serializer = FilesSerializer(lists, many=True)
        return Response(serializer.data)


class UpFile(generics.CreateAPIView):
    serializer_class = UpFileSerializer
