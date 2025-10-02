# Projeto Dolar Agora — Novas Mudanças e Biblioteca

🎧 **Música Recomendada:**  
Para se concentrar na identificação e mitigação de riscos de segurança, ouça:  
["River" — Ouça no YouTube](https://www.youtube.com/watch?v=V-uTOWL8X0w)

![Thorfin](images/thorfin.png)

---

## Resumo das Mudanças

Este projeto passou por diversas melhorias para garantir maior disponibilidade, integridade dos dados e experiência do usuário. Veja abaixo as principais alterações:

### 1. Nova Biblioteca de Cotação: `pycotacao`

- Adicionada a biblioteca [pycotacao](https://pypi.org/project/pycotacao/) para buscar a cotação do dólar diretamente no backend Django.
- O backend agora tenta obter o valor via pycotacao e, em caso de falha, ativa o failover para buscar via JavaScript (AwesomeAPI).

### 2. Redundância e Failover

- Implementada rota `/dolar_agora_redundancia` que utiliza pycotacao.
- Se o backend não conseguir obter a cotação, o frontend automaticamente busca o valor usando a AwesomeAPI via JavaScript, garantindo disponibilidade.

### 3. Atualização dos Templates

- O template `dolar_agora.html` foi aprimorado para exibir o valor do dólar, variação, status da consulta e fonte dos dados.
- Adicionado botão de atualização manual e lógica para exibir mensagens de erro ou sucesso conforme a fonte dos dados.

### 4. Novas Dependências

- Atualizado o arquivo `requirements.txt` para incluir pycotacao.
- Certifique-se de instalar as dependências com:
  ```sh
  pip install -r requirements.txt
  ```

### 5. Organização das Rotas

- O arquivo `urls.py` agora possui rotas separadas para a página principal, visualização da cotação e redundância.

### 6. Documentação e Imagens

- Adicionada documentação explicando o funcionamento da redundância e failover.
- Imagem ilustrativa incluída para representar o novo ciclo do projeto.

---

## Como funciona a redundância

1. O usuário acessa `/dolar_agora_redundancia`.
2. O backend tenta buscar a cotação via pycotacao.
3. Se houver erro, o frontend busca automaticamente via AwesomeAPI.
4. O usuário sempre recebe o valor mais atualizado possível, mesmo em caso de falha de uma das fontes.

---

Essas mudanças tornam o sistema mais robusto, confiável e preparado para lidar com falhas externas, além de melhorar a experiência do usuário.