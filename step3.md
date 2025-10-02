# Passo 3: Implementação do Frontend e Interfaces

Nesta etapa, criamos as duas interfaces principais que definem a experiência do usuário, utilizando diferentes frameworks CSS para exibir a cotação do Dólar.

Para dar um toque especial ao seu desenvolvimento frontend, a sugestão sonora para esta etapa é:

"Giorno's Theme (Il Vento D'oro)" — [Ouça no YouTube](https://www.youtube.com/watch?v=U0TXIXTzJEY&list=RDGMEMCMFH2exzjBeE_zAHHJOdxgVMU0TXIXTzJEY&index=1)

![Giorno Giovanna](images/giorno_giovanna.png)

---

## 1. Página Inicial (`core/index.html`)

**Função:**  
Serve como ponto de entrada (`/`) do projeto, apresentando o propósito da aplicação (Dolar Agora) e convidando o usuário a verificar a cotação.

**Tecnologia:**  
- **Tailwind CSS:** Framework utilitário para um visual moderno, centralizado e responsivo. Utiliza classes simples para garantir carregamento rápido e transição suave para a página de cotação.

**Resumo do Template:**  
- Card principal centralizado  
- Título chamativo  
- Botão de ação ("Ver Cotação Agora") que direciona para `/dolar_agora`

---

## 2. Visualizador de Cotação (`core/dolar_agora.html`)

**Função:**  
Exibe o valor do Dólar Comercial (USD/BRL), variação percentual (indicando alta ou baixa) e o momento da última atualização.

**Tecnologia:**  
- **Bootstrap 5:** Utilizado para o layout do card e aplicação de estilos prontos (`card`, `text-primary`, `bg-light`)
- **JavaScript nativo (Fetch API):** Responsável por buscar os dados em tempo real

**Resumo do Funcionamento:**  
- O JavaScript faz requisição assíncrona (`fetch`) para a API pública de cotação (`economia.awesomeapi.com.br`)
- Processa o JSON da resposta
- Atualiza o valor (`#dolar-value`), a hora (`#last-update`) e a cor da variação (verde para positivo, vermelho para negativo) diretamente no HTML (DOM)
- O script principal chama `fetchDolarRate()` no `window.onload` para carregar o valor inicial e permite atualização manual via botão "Atualizar Agora"

---

Essas duas páginas garantem uma experiência fluida e informativa ao usuário, combinando design moderno com dados em tempo real.