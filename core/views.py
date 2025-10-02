from django.shortcuts import render
from pycotacao import get_exchange_rates, CurrencyCodes
import logging

# Configura o logger para a view (ajuda a ver erros no console do Django)
logger = logging.getLogger(__name__)

def home(request):
    """Renderiza a página inicial (Home)."""
    return render(request, 'core/index.html')

def dolar_agora_api(request):
    """
    Busca a cotação do Dólar usando a API pycotacao.
    Retorna o valor para o template.
    """
    context = {}
    
    try:
        # 1. Busca o objeto de cotação do Dólar (USD)
        taxa_dolar_obj = get_exchange_rates(CurrencyCodes.USD)
        
        # 2. Extrai o valor de venda (selling_rate)
        # O valor de venda é o mais comum para cotações públicas.
        taxa_venda = taxa_dolar_obj.selling_rate
        
        # 3. Formata e prepara o contexto para o template
        context['dolar_value'] = f"R$ {taxa_venda:.4f}"
        context['status_message'] = "Cotação obtida com sucesso via Backend (pycotacao)."
        context['error'] = False # Não houve erro, desativa o failover JS
        
    except Exception as e:
        logger.error(f"Falha ao buscar cotação via pycotacao: {e}")
        
        # Prepara o contexto de erro para ativar o failover JS no template
        # Isso garante que a aplicação tente buscar a cotação via JavaScript (AwesomeAPI)
        context['dolar_value'] = 'ERRO'
        context['status_message'] = "Falha no servidor. Carregando via JavaScript..."
        context['error'] = True # Ativa o failover JS

    return render(request, 'core/dolar_agora.html', context)

def dolar_agora(request):
    return render(request, 'core/dolar_agora.html')

def home(request):
    return render(request, 'core/index.html')