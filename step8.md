# Projeto Dolar Agora — Novo Banco de Dados

🎧 **Música Recomendada:**  
Para se concentrar na criação de banco de dados:  
["Samurai Champloo - Shiki No Uta (HQ)"](https://www.youtube.com/watch?v=cNplZrRSjeI&list=RDcNplZrRSjeI)

---

## 🚀 Motivação

Chamar APIs de terceiros (como pycotacao) a cada requisição do usuário é ineficiente e pode gerar custos ou exceder limites.  
Esta mudança introduz um mecanismo de cache baseado em tempo no banco de dados: o sistema só faz nova chamada à API se a última cotação salva for mais antiga que um período definido (1 minuto, neste teste).

---

## 🛠️ Mudanças Principais

As alterações foram divididas em três arquivos principais:

- **views.py:** Implementação da lógica de cache e fallback de erro.
- **models.py:** Definição formal do modelo CotacaoDolar.
- **admin.py:** Registro do novo modelo no painel de administração do Django.

---

### 1. views.py — Otimização com Caching

A view `dolar_agora_api` foi reestruturada para seguir a lógica "cache-aside":

| O que mudou         | Descrição                                                                 |
|---------------------|---------------------------------------------------------------------------|
| Importações         | Adicionadas para cache: logging, CotacaoDolar, timedelta, timezone.        |
| Inicialização       | Logging configurado para registrar falhas da API, melhorando o debug.      |
| Definição do Cache  | Constante `TEMPO_CACHE = timedelta(minutes=1)`. Em produção, aumente esse valor. |
| Lógica de Checagem  | Verifica se existe cotação recente no banco antes de chamar a API.         |
| Cache HIT           | Se o cache for válido, usa o valor salvo e evita chamada à API.            |
| Cache MISS          | Se o cache estiver expirado, chama a API, salva novo registro e usa o valor.|
| Tratamento de Erros | Contexto de erro enviado ao template se API falhar ou cache estiver vazio. |
| Limpeza             | Removido código duplicado de contexto.                                     |

---

### 2. models.py — Estruturação do Modelo

A classe `CotacaoDolar` foi movida para o arquivo models.py.

| O que mudou | Descrição                                                                 |
|-------------|---------------------------------------------------------------------------|
| Campos      | Mantidos: valor (DecimalField), data_registro (DateTimeField), fonte.     |
| __str__     | Método de representação amigável do objeto.                               |
| Meta        | Ordenação por data_registro decrescente para facilitar busca do cache.    |

---

### 3. admin.py — Registro no Painel Admin

Adicionada importação e registro da classe CotacaoDolar:

```python
from django.contrib import admin
from .models import CotacaoDolar

admin.site.register(CotacaoDolar)
```

Isso permite visualizar, editar e gerenciar o histórico de cotações diretamente no painel de administração do Django.

---

## ⚠️ Ações Necessárias Pós-Merge (Deploy)

Para que as mudanças entrem em vigor:

1. **Migrações:**  
   Gere e aplique as migrações do banco de dados:
   ```sh
   python manage.py makemigrations [nome_do_seu_app]
   python manage.py migrate
   ```

2. **Teste de Cache:**  
   - 1º acesso à view: Deve indicar "Cotação atualizada, buscada da API externa."
   - 2º acesso (imediato): Deve indicar "Cotação obtida do cache do Banco de Dados."
   - 3º acesso (após 1 minuto): Deve voltar a buscar na API.

---

Essas mudanças tornam o sistema mais eficiente, seguro e preparado para produção.
