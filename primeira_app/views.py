from django.shortcuts import render     # Biblioteca que permite renderizar um tamplate (arquivo .html)

# - Todas as views são criadas aqui;
# - Cada view é uma função que recebe uma requisição HTTP e retorna uma resposta HTTP;
# - Para dizer quando esta função deve ser chamada, deve-se definir a rota dela em urls.py.

def render_index_template(request):
    # Renderiza o arquivo index_primeira_app.html dentro de primeira_app/templates/primeira_app/
    return render(request, "primeira_app/index_primeira_app.html")    # No caminho não deve-se colocar "templates" porque o Django já procura nesta pasta

def render_static_template(request):
    # Renderiza o arquivo static_template_app.html dentro de primeira_app/templates/primeira_app/
    return render(request, "primeira_app/static_template_app.html")

def render_dinamic_template(request):

    contexto = {
        'nome': 'William',
        'idade': 23,
        'cidade': 'Recife'
    }

    # Renderiza o HTML dinâmico substituindo as chaves do dicionário contexto que estão dentro de {{}} pelos seus valores
    return render(request, "primeira_app/dinamic_template_app.html", contexto)
