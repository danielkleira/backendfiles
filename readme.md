# desafiofullstacksS1

## ✨ Projeto

Este projeto tem como base o envio de um arquivo CNAB e seu respectivo salvamento num banco de dados.

## 🚀 Tecnologias

Esse projeto foi desenvolvido com as seguintes tecnologias/bibliotecas:

<table border="0">
 <tr>
<td> Python</td>
<td> Django</td>
<td> SQlite3</td>
 </tr>
</table>

## 👨🏻‍💻 Executando o projeto

Utilize o **pip install django** e o **pip install -r requeriments.txt** para instalar as dependências do projeto frontend. <br>
Em seguida, inicie o projeto no navegador rodando **python manage.py runserver** <br>
Agora seu projeto deve estar na página **http://localhost:8000/api/file/** <br>
Escolha um arquivo CNAB.txt e o suba clicando em POST<br>
Assim seu arquivo estará salvo temporariamente<br>

Para salva-lo no banco de dados, vá para a página **http://localhost:8000/api/file/list** <br>
Aqui você pode realizar um GET e listar o que já tem no banco de dados, ou realizar um POST, transferindo os dados do arquivo para o banco de dados SQLITE3. <br>
Ao realizar um POST, seu arquivo é excluido enquanto é transferido para o banco de dados.
