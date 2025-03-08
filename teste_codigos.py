def busca_binaria(vetor, inicio, fim, x):
    while inicio <= fim:
        m = (inicio + fim) // 2  # Encontra o meio do vetor

        if x == vetor[m]:  
            return m  # Retorna a posição se encontrou
        
        elif x > vetor[m]:  
            inicio = m + 1  # Busca na metade direita  
        
        else:  
            fim = m - 1  # Busca na metade esquerda  

    return -1  # Retorna -1 se não encontrar

# Entrada do usuário com tratamento de erro
try:
    x = int(input("Digite um número para buscar: "))
except ValueError:
    print("Erro: Por favor, digite um número válido.")
    exit()  # Sai do programa se o usuário digitou algo inválido

# Vetor de exemplo
vetor = [1, 3, 5, 7, 9, 11, 13]

# Chamada da função
resultado = busca_binaria(vetor, 0, len(vetor) - 1, x)

# Exibir o resultado
if resultado != -1:
    print(f"Número encontrado na posição {resultado}.")
else:
    print("Número não encontrado.")
