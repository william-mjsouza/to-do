from django.db import models

# - Aqui são colocados todos os modelos da app;
# - Todo modelo deve ser uma classe do Python com um nome no singular, sem separador e que se refere a funcionalidade da app;
# - Todo modelo deve herdar de uma outra classe do Django (models.Model);
# - Um modelo também pode ser pensado como a representação do banco de dados, onde cada coluna é um atributo da classe
#   e cada linha é uma instância dessa classe;
# - O Djando abstrai todas as operações no banco de dados por meio dos modelos (não precisa escrever em SQL);
# - Após criar ou atualizar algo no modelo, deve-se fazer uma migração:
#   python manage.py makemigrations     (procura diferenças)
#   python manage.py migrate            (caso tenha diferenças, faz a migração)

# Classe que abstrai uma tarefa de uma lista de tarefas
class ToDo(models.Model):
    # Título da tarefa
    title = models.CharField(max_length=100, null=False, blank=False) # Máximo de 100 caracteres, não pode ser um enter e não pode ter apenas espaços
    # Data de criação da tarefa
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False) # Formato de data (dd/mm/aaaa), é preenchido automaticamente
    # Data de entrega da tarefa
    deadline = models.DateTimeField(null=False, blank=False) # usuário é que define a data (não pode ser automático)
    # Data de finalização da tarefa
    finished_at = models.DateTimeField(null=True, blank=False) # Pode ser nulo pro usuário preencher depois