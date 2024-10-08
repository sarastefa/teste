import panda as pd

produtosdf = pd.DataFrame(columns=['Código', 'Nome', 'Quantidade', 'Preço'])

def cadastrarproduto():
    global produtosdf
    while True:
        codigo = input("Digite o código do produto: ")
        nome = input("Digite o nome do produto: ")
        quantidade = int(input("Digite a quantidade em estoque: "))
        preco = float(input("Digite o preço por unidade: "))
  
produtosdf = produtosdf.append({'Código': codigo, 'Nome': nome, 'Quantidade': quantidade, 'Preço': preco}, ignore_index=True)

while True:
    continuar = input("Deseja cadastrar mais um produto? (sim/não): ").strip().lower()
      if continuar == 'não':
        break
with open('relatorioEstoque.txt', 'w') as arquivo:
    arquivo.write("codigo\tnome\tquantidade\tpreco\n")
    for p in produtos:
        arquivo.write(f"{p['código']}\t{p['nome']}\t{p['quantidade']}\t{p['preço']:.2f}\n")
      
def registrarvenda():
    global produtosdf
    totalvendas = 0.0

    while True:
        nomevenda = input("Digite o nome do produto que deseja : ").strip()
      try:
        quantidadevendida = int(input("Digite a quantidade a ser vendida: "))

if nomevenda not in produtosdf['Nome'].values:
            print("Produto não encontrado.")
            continue
  
 estoquedispon = produtosdf.loc[produtosdf['Nome'] == nomevenda, 'Quantidade'].values[0]

if quantidadevendida > estoquedispon:
    print("Estoque não é suficiente.")
    continue

valortotal = quantidadevendida * preco
totalvendas += valortotal

produtosdf.loc[produtosdf['Nome'] == nomevenda, 'Quantidade'] -= quantidadevendida
print(f"Venda registrada: {quantidadevendida} de '{nomevenda}'.")

vendasrealizadas.append({
            'Código': produtosdf.loc[produtos_df['Nome'] == nomevenda, 'Código'].values[0],
            'Nome': nomevenda,
            'Quantidade': quantidadevendida,
            'Valor Total': valortotal
        })

continuar = input("Deseja registrar outra venda? (sim/não): ").strip().lower()
if continuar != 'sim':
    break

 if vendas_realizadas:
        vendasdf = pd.DataFrame(vendasrealizadas)
        vendasdf.to_csv('relatorioVendas.csv', index=False)
        print("\nRelatório gerado: relatorioVendas.csv")
