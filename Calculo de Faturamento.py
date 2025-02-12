import pandas as pd

def calcular_faturamento(nome_arquivo):
    """
    Calcula o faturamento total por produto e encontra os produtos com maior e menor faturamento.

    Args:
        nome_arquivo (str): O nome do arquivo CSV contendo os dados de vendas.

    Returns:
        tuple: Uma tupla contendo:
            - pandas.Series: Faturamento total por produto.
            - str: Produto com maior faturamento.
            - str: Produto com menor faturamento.
    """
    try:
        df = pd.read_csv(nome_arquivo)  # Lê o arquivo CSV
    except FileNotFoundError:
        return "Arquivo não encontrado.", None, None  # Trata erro de arquivo

    # Calcula o faturamento para cada linha e armazena numa nova coluna
    df['faturamento'] = df['quantidade'] * df['preco_unitario']

    # Calcula o faturamento total por produto
    faturamento_por_produto = df.groupby('produto')['faturamento'].sum()

    if faturamento_por_produto.empty: # Verifica se o df está vazio após o calculo
      return "Não há dados para calcular o faturamento", None, None

    # Encontra o produto com maior e menor faturamento
    maior_faturamento = faturamento_por_produto.idxmax()
    menor_faturamento = faturamento_por_produto.idxmin()

    return faturamento_por_produto, maior_faturamento, menor_faturamento


# Nome do arquivo CSV (substitua pelo nome real do seu arquivo)
nome_arquivo = 'vendas.csv' 

faturamento, produto_maior, produto_menor = calcular_faturamento(nome_arquivo)

if isinstance(faturamento, str):  # Verifica se houve algum erro
  print(faturamento) # Imprime a mensagem de erro
else:
  print("Faturamento por produto:\n", faturamento)
  print("\nProduto com maior faturamento:", produto_maior)
  print("Produto com menor faturamento:", produto_menor)