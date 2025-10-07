# Projeto Dolar Agora — Novas Mudanças e Biblioteca

🎧 **Música Recomendada:**  
Para se concentrar na identificação e mitigação de riscos de segurança, ouça:  
["Bôa - Duvet" — Ouça no YouTube](https://www.youtube.com/watch?v=8cUhlIEUjOI)

---

## Resumo das Mudanças

Agora a SECRET_KEY do Django é obtida a partir de uma variável de ambiente, aumentando a segurança do projeto.

### Como definir a SECRET_KEY

**Windows (PowerShell):**
```sh
$env:SECRET_KEY="sua-chave-secreta-aqui"
python manage.py runserver
```

**Linux / macOS (Terminal):**
```sh
export SECRET_KEY="sua-chave-secreta-aqui"
python manage.py runserver
```

Dessa forma, a chave secreta não fica exposta no código-fonte, seguindo boas práticas de segurança.