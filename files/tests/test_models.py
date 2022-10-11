from django.test import TestCase
from ..models import UpFile, Files


class AccountTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        with open("testsFile.txt", "r") as line:
            lines = line.readlines()
        for i in lines:
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
        cls.user = Files.objects.create(
            tipo=tipo,
            data=dataPt1 + "/" + dataPt2 + "/" + dataPt3,
            valor=valor,
            cpf=cpf,
            cartao=cartao,
            hora=hora,
            dono_da_loja=dono_da_loja,
            nome_loja=nome_loja,
        )
        
    def test_create_type(self):
        self.assertEquals(self.user.tipo,"3")
    
    def test_create_value(self):
        self.assertEquals(self.user.valor,192.0)
        
    def test_create_owner(self):
        self.assertEquals(self.user.dono_da_loja,"MARCOS PEREIRA")
    
    def test_create_store(self):
        self.assertEquals(self.user.nome_loja,"MERCADO DA AVENIDA")

