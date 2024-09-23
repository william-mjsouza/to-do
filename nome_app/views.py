from django.shortcuts import render     # Biblioteca que permite renderizar um tamplate (arquivo.html)

# Todas as views são criadas aqui.
# Cada view é uma função que recebe uma requisição e envia uma resposta
# Para dizer quando esta função deve ser chamada, deve-se definir a rota dela
def render_template(request):
    # Renderiza o arquivo template_app.html dentro de nome_app/templates/nome_app/
    return render(request, "nome_app/template_app.html")    # No caminho não deve-se colocar "templates" porque o Django já procura nesta pasta