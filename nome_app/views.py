from django.shortcuts import render     # Biblioteca que permite renderizar um tamplate html
from django.http import HttpResponse    # Biblioteca que tem a função HttResponse (retorna uma mensagem tag html)

# Todas as views são criadas aqui.
# Cada view é uma função que recebe uma requisição e envia uma resposta
# Para dizer quando esta função deve ser chamada, deve-se definir a rota dela
def home(request):
    return render(request, "nome_app/home.html")    # No caminho não deve-se colocar "templates" porque o Django já procura nesta pasta