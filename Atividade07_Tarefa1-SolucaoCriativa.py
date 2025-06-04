# Atividade Prática 1-  Leia um arquivo que 
# contém dados de log de treinamento de modelos 
# de Machine Learning. Calcule a média e o 
# desvio padrão do tempo de execução constantes. 

# R - LEITURA
# A - INCREMENTAR
# W - ESCRITA
# X - CRIAR
# R+ - LEITURA + ESCRITA
 
nome_arquivo = 'logs_treinamento.csv'
nome_coluna = 'tempo_execucao'
separador = ','

valores_coluna = []
with open(nome_arquivo, 'r') as f:
    cabecalho = f.readline().strip().split(separador)
    indice_coluna = cabecalho.index(nome_coluna) # Isso vai dar erro se a coluna não existir!

    for linha in f:
        partes = linha.strip().split(separador)
        try:
            # Pega o valor da coluna e tenta converter para número
            valores_coluna.append(float(partes[indice_coluna]))
        except (ValueError, IndexError):
            # Ignora linhas com valor não numérico ou coluna faltando
            pass

# Cálcula a Média
media = sum(valores_coluna) / len(valores_coluna) if valores_coluna else 0.0

# 4. Calcula o Desvio Padrão
# Cálculo da variância (soma dos quadrados das diferenças / N)
variancia = sum([(x - media) ** 2 for x in valores_coluna]) / len(valores_coluna)

# Cálculo do desvio padrão (raiz quadrada da variância, sem 'math.sqrt')
desvio_padrao = variancia ** 0.5

# Resultado Exibido
print(f"\nA média da coluna '{nome_coluna}' é: {media:.2f}")
print(f"O desvio padrão da coluna '{nome_coluna}' é: {desvio_padrao:.2f}\n")