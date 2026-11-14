# 📦 Desafio de Aprendizado: Cadastro de Produtos com Dicionários

## 📖 Sobre o Projeto

Este projeto foi desenvolvido como parte de uma **jornada de aprendizado em Python**, com o objetivo de consolidar o uso de **dicionários**, **loops aninhados**, **tratamento robusto de exceções** e **formatação de strings**.

O programa simula um sistema de cadastro de produtos, onde o usuário insere o nome e o valor de cada item. O sistema garante que apenas valores numéricos válidos sejam aceitos antes de prosseguir, exibindo ao final um resumo formatado da compra.

---

## 🎯 Objetivo do Desafio

Praticar e fixar os seguintes conceitos:
- ✅ Criação e manipulação de dicionários (`{}`, `chave = valor`)
- ✅ Loops aninhados (`while` dentro de `while`) para validação granular
- ✅ Tratamento de exceções com `try/except ValueError`
- ✅ Iteração sobre dicionários com o método `.items()`
- ✅ Formatação de números decimais para padrão monetário (`:.2f`)

---

## 🧩 Elementos do Código e Seus Objetivos

| Elemento | Objetivo Principal |
|---|---|
| `produtos = {}` | Inicializa um dicionário vazio para armazenar os pares `nome: preço`. |
| `while True:` (externo) | Controla o fluxo principal de cadastro de novos produtos. |
| `nome.lower() == "sair"` | Condição de parada case-insensitive para encerrar o cadastro. |
| `while True:` (interno) | Isola a validação do preço, repetindo a pergunta até que a entrada seja válida. |
| `float(input(...).strip())` | Converte a entrada para número decimal, removendo espaços acidentais. |
| `except ValueError:` | Captura erros de digitação (letras, símbolos) e impede a quebra do programa. |
| `produtos[nome] = preco` | Associa o nome do produto ao seu preço validado no dicionário. |
| `for nome, preco in produtos.items():` | Desempacota e percorre simultaneamente as chaves e valores do dicionário. |
| `total += preco` | Acumulador que soma o valor de todos os produtos iterados. |
| `:.2f` | Formata o número float para exibir exatamente 2 casas decimais (padrão de moeda). |

---

## 💻 Como Executar

### Pré-requisitos
- Python 3.x instalado ([python.org](https://www.python.org/))

### Passos
```bash
# Salve o código em um arquivo, por exemplo: cadastro_produtos.py
# Execute no terminal:
python cadastro_produtos.py
```

---

## 🖥️ Exemplo de Execução

```text
Digite aqui o nome do produtos: Arroz
Valor do produto: 5.50
Digite aqui o nome do produtos: Feijão
Valor do produto: abc
Digite valores apenas em decimais
Valor do produto: 8
Digite aqui o nome do produtos: sair

Seus produtos foram os seguintes: 
Arroz: R$ 5.50
Feijão: R$ 8.00

Total da compra foi de R$13.50
```

---

## 📚 Conceitos Aprendidos

1. **Dicionários como Banco de Dados Simples:** Associação direta entre uma chave única (nome) e um valor (preço).
2. **Validação em Loop (Nested Loops):** Uso de um `while` interno para garantir a qualidade dos dados antes de permitir que o fluxo principal avance.
3. **Resiliência a Erros:** O programa não quebra com entradas inválidas, orientando o usuário a corrigir o erro.
4. **Iteração Eficiente:** Uso de `.items()` para acessar chaves e valores simultaneamente, evitando buscas redundantes no dicionário.

---

## 👨‍💻 Autor

**Victor** — Estudante de Programação Python

## 📜 Licença

Projeto desenvolvido para fins educacionais. Livre para estudo e adaptação.
