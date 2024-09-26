from django.shortcuts import render, redirect
from datetime import datetime
from django.utils import timezone
from .models import Commitment

def render_calendar(request):
    return render(request, "segunda_app/calendar_page.html")

def add_commitment(request):
    # Captura a data selecionada do calendário
    date_str = request.GET.get('date')  # A data vem como um parâmetro GET do calendário

    if request.method == 'POST':
        try:
            # Converte a data de 'd/m/Y' para o formato esperado pelo Django 'Y-m-d'
            date_obj = datetime.strptime(date_str, '%d/%m/%Y')  # Exemplo: '28/09/2024'
            
            # Combina a data com a hora de início e fim para gerar os datetime completos
            start_time = datetime.combine(date_obj, datetime.strptime(request.POST['hora_inicio'], '%H:%M').time())
            
            # Verifica se a hora de fim foi passada, caso contrário, use 23:59 como padrão
            end_time = datetime.combine(date_obj, datetime.strptime(request.POST.get('hora_fim', '23:59'), '%H:%M').time())
            
            # Torna as datas timezone-aware para evitar os warnings de naive datetime
            start_time = timezone.make_aware(start_time)
            end_time = timezone.make_aware(end_time)
            
            # Cria o compromisso no banco de dados
            Commitment.objects.create(
                time_start=start_time,
                time_end=end_time,
                processes=request.POST['processo'],
                location=request.POST['local'],
                description=request.POST['observacoes']
            )
            return redirect('agenda')  # Redireciona para a agenda após salvar o compromisso
        except ValueError:
            # Caso a data ou hora esteja em um formato inválido, retorna uma mensagem de erro
            return render(request, "segunda_app/add_commitment_page.html", {
                'selected_date': date_str,
                'error': 'Formato de data ou hora inválido. Tente novamente.'
            })

    # Passa a data selecionada para o template de adição de compromisso
    return render(request, "segunda_app/add_commitment_page.html", {'selected_date': date_str})
