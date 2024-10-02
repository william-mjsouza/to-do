from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect

def show_ip(request):
    # Tenta obter o IP do cabeçalho X-Forwarded-For (no caso de proxy), caso contrário, use REMOTE_ADDR
    ip_address = request.META.get('HTTP_X_FORWARDED_FOR')
    if ip_address:
        ip_address = ip_address.split(',')[0]  # Caso existam múltiplos IPs no cabeçalho, pegar o primeiro
    else:
        ip_address = request.META.get('REMOTE_ADDR')

    # Retorna uma página simples mostrando o IP
    return HttpResponse(f'Seu endereço IP é {ip_address}')


def custom_template_based_on_ip(request):
    # Definir IPs específicos para renderizar diferentes templates
    specific_ip = '192.168.0.60'  # Exemplo de um IP local específico
    ip_address = request.META.get('HTTP_X_FORWARDED_FOR')
    
    if ip_address:
        ip_address = ip_address.split(',')[0]  # Pegando o primeiro IP no cabeçalho
    else:
        ip_address = request.META.get('REMOTE_ADDR')

    # Verifica se o IP corresponde ao específico e renderiza o template correto
    if ip_address == specific_ip:
        return render(request, 'terceira_app/template_for_specific_ip.html')
    else:
        return render(request, 'terceira_app/default_template.html')


def restrict_access_by_ip(request):
    blocked_ips = ['192.168.1.101', '192.168.1.102']  # Lista de IPs bloqueados
    ip_address = request.META.get('HTTP_X_FORWARDED_FOR')
    
    if ip_address:
        ip_address = ip_address.split(',')[0]
    else:
        ip_address = request.META.get('REMOTE_ADDR')

    # Se o IP estiver na lista de IPs bloqueados, retornamos uma resposta 403 (Forbidden)
    if ip_address in blocked_ips:
        return HttpResponseForbidden("Acesso negado.")

    # Se for um IP específico, redireciona para uma outra página
    if ip_address == '192.168.0.60':
        return HttpResponseRedirect('agenda')

    # Caso contrário, renderiza a página normal
    return HttpResponse(f'Seu IP é {ip_address}. Acesso permitido.')
