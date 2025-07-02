cadastros = []

while True:
    nome = input("Digite o nome (ou 'sair' para encerrar): ")
    if nome.lower() == 'sair':
        break

    idade = int(input("Digite a idade: "))
    cidade = input("Digite a cidade: ")

    pessoa = {
        "nome": nome,
        "idade": idade,
        "cidade": cidade
    }

    cadastros.append(pessoa)

# Total de pessoas
print(f"\nTotal de pessoas cadastradas: {len(cadastros)}")

# Cidades únicas
cidades = set()
for pessoa in cadastros:
    cidades.add(pessoa["cidade"])

print("Cidades únicas:")
for cidade in cidades:
    print("-", cidade)

# Busca por nome (opcional)
busca = input("\nDigite um nome para buscar (ou pressione Enter para pular): ")
if busca:
    encontrou = False
    for pessoa in cadastros:
        if pessoa["nome"].lower() == busca.lower():
            print(f"{pessoa['nome']} tem {pessoa['idade']} anos e mora em {pessoa['cidade']}.")
            encontrou = True
            break
    if not encontrou:
        print("Pessoa não encontrada.")
