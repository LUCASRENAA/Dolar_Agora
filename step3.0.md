# Passo Adicional: Entendendo a Estrutura HTML

Como o seu projeto Django utiliza arquivos HTML para a interface, é fundamental entender o papel do HTML e como ele serve de base para o design com Bootstrap e Tailwind CSS.

## O que é HTML?

HTML (HyperText Markup Language) é uma linguagem de marcação usada para estruturar páginas web.  
Ela define o conteúdo e a hierarquia: títulos, parágrafos, botões, links e imagens.

## Estrutura Básica de uma Página HTML

Toda página HTML segue um formato padrão, utilizando tags para envolver o conteúdo:

```html
<!DOCTYPE html> <!-- Define que o documento é HTML5 -->
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Título da Página</title>
    <!-- Links para Bootstrap ou Tailwind entram aqui -->
</head>
<body>
    <h1>Este é um título principal</h1>
    <p>Este é um parágrafo de texto.</p>
    <button>Clique Aqui</button>
</body>
</html>
```

## Tags Semânticas Comuns

| Tag         | Função                                   | Exemplo                       |
|-------------|------------------------------------------|-------------------------------|
| `<h1>`-`<h6>` | Títulos (do mais ao menos importante)    | `<h1>Dólar Agora</h1>`        |
| `<p>`       | Parágrafo de texto                       | `<p>Cotação em tempo real.</p>`|
| `<div>`     | Contêiner genérico para layout           | `<div class="card">...</div>` |
| `<a>`       | Link para navegação                      | `<a href="/dolar_agora">Ver Cotação</a>` |
| `<img>`     | Imagem                                   | `<img src="caminho/imagem.png">` |

## Exemplo de Página Simples: Card da Home

O arquivo `core/index.html` é um exemplo de página simples. Ele usa `<div>` para criar um card centralizado e `<a>` como botão de navegação.

```html
<!-- Exemplo simplificado de index.html -->
<body class="bg-gray-50">
    <div class="max-w-md bg-white p-8">
        <h1>Dólar Agora 💸</h1>
        <p>Sua ferramenta para cotação...</p>
        <a href="/dolar_agora">Ver Cotação Agora</a>
    </div>
</body>
```

Ao dominar essas tags e entender que elas definem a estrutura, você pode usar frameworks CSS (como Bootstrap ou Tailwind) para transformar páginas simples em interfaces modernas, como nas páginas `index.html` e `dolar_agora.html`.