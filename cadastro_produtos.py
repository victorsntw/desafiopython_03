produtos = {} # dicionário vazio para guardar nomes e preços

while True: # laço de repetição
    nome = input("Digite aqui o nome do produtos: ").strip() # váriável para guardar os nomes

    if nome.lower() == "sair": # verifica se o nome é "Sair"
        break # se for sair o sistema para e pula para o LOOP
    while True:
        try: # tratamento de erro
            preco_produto = float(input("Valor do produto: ").strip()) # pede o valor do prduto em decimal
            break
        except ValueError: # tratamento de erros
            print("Digite valores apenas em decimais") # exibe essa mensagem caso não seja números.

    produtos[nome] = preco_produto # adiciona o nome e o preço no dicionário

total = 0 # várialve para calcular o valor total
print("Seus produtos foram os seguintes: ")
for nome, preco in produtos.items(): # LOOP - para percorrer o dicionário para exibir o nom e o preço
    print(f"{nome}: R$ {preco:.2f}")
    total += preco # adiciona no total o preço e faz uma soma

print(f"\nTotal da compra foi de R${total:.2f}") # exibe o valor total das compras