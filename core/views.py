from django.shortcuts import render
from pycotacao import get_exchange_rates, CurrencyCodes
import logging
from .models import CotacaoDolar
from datetime import timedelta
from django.utils import timezone
# Configura o logger para a view (ajuda a ver erros no console do Django)
logger = logging.getLogger(__name__)

def home(request):
    """Renderiza a página inicial (Home)."""
    return render(request, 'core/index.html')

def dolar_agora_api(request):
    taxa_venda = None
    context =  {}

    try:
        # 1. Tenta buscar a cotação mais recente salva no banco de dados.
        #    O método .first() retorna o objeto mais recente ou None.
        ultima_cotacao = CotacaoDolar.objects.order_by('-data_registro').first()
        TEMPO_CACHE = timedelta(minutes=1)
        # O momento em que a cotação salvaria/buscou
        momento_atual = timezone.now()
        print("teste")
        # 2. Verifica se a última cotação existe E se ela ainda é válida
        if ultima_cotacao and (ultima_cotacao.data_registro + TEMPO_CACHE > momento_atual):
            # COTAÇÃO VÁLIDA: Usa o valor do banco de dados (Cache HIT)
            taxa_venda = ultima_cotacao.valor
            context['status_message'] = "Cotação obtida do cache do Banco de Dados."
        else:
            # COTAÇÃO EXPIRADA OU INEXISTENTE: Chama a API (Cache MISS)
            
            # --- CHAMA API EXTERNA ---
            taxa_dolar_obj = get_exchange_rates(CurrencyCodes.USD)
            taxa_venda_api = taxa_dolar_obj.selling_rate
            # -------------------------
            
            # Salva a nova cotação no banco de dados
            CotacaoDolar.objects.create(
                valor=taxa_venda_api,
                fonte="pycotacao" # Opcional: use o campo fonte
            )
            
            taxa_venda = taxa_venda_api
            context['status_message'] = "Cotação atualizada, buscada da API externa."
        
        # 3. Prepara o contexto de resposta
        if taxa_venda is not None:
            context['dolar_value'] = f"R$ {taxa_venda:.4f}"
            context['error'] = False
        else:
             # Caso a API tenha falhado, mas o cache também estava vazio
            context['status_message'] = "Erro ao obter a cotação da API e cache vazio."
            context['error'] = True
        
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


def grafico_dolar_view(request):
    """
    Busca todas as cotações salvas e prepara os dados para o gráfico.
    """
    
    # 1. Busca todos os objetos de cotação, ordenados do mais antigo ao mais novo
    historico_cotacoes = CotacaoDolar.objects.all().order_by('data_registro')

    # 2. Inicializa as listas que serão usadas como Labels (Datas) e Dados (Valores)
    datas = []
    valores = []

    # 3. Itera sobre o histórico para popular as listas
    for cotacao in historico_cotacoes:
        # Formata a data para um formato legível no gráfico (ex: 2025-10-06 14:30)
        data_formatada = cotacao.data_registro.strftime('%Y-%m-%d %H:%M')
        
        # O valor é convertido para float para ser melhor manipulado pelo JS
        valor_float = float(cotacao.valor)
        
        datas.append(data_formatada)
        valores.append(valor_float)

    # 4. Cria o contexto para enviar os dados ao template
    contexto = {
        'datas_labels': datas,      # Lista de datas/horários
        'valores_data': valores,    # Lista dos valores do Dólar
        'quantidade_registros': historico_cotacoes.count()
    }

    return render(request, 'core/grafico_dolar.html', contexto)
