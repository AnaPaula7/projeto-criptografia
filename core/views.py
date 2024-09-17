from django.shortcuts import render
from .forms import CriptografiaForm

# Definimos o alfabeto e os números como strings
alfabeto = 'abcdefghijklmnopqrstuvwxyz'
numeros = '0123456789'

# Função para criptografar a mensagem
def criptografar(mensagem, chave):
    resultado = []  # Lista para armazenar o resultado criptografado
    
    # Percorre cada caractere da mensagem
    for char in mensagem:
        if char.lower() in alfabeto:  # Verifica se o caractere é uma letra
            # Pega a posição da letra no alfabeto
            posicao = alfabeto.index(char.lower())
            # Calcula a nova posição deslocada
            nova_posicao = (posicao + int(chave)) % len(alfabeto)
            # Adiciona a nova letra ao resultado, mantendo maiúscula/minúscula
            if char.isupper():
                resultado.append(alfabeto[nova_posicao].upper())
            else:
                resultado.append(alfabeto[nova_posicao])
        elif char in numeros:  # Verifica se o caractere é um número
            # Pega a posição do número
            posicao = numeros.index(char)
            # Calcula a nova posição deslocada
            nova_posicao = (posicao + int(chave)) % len(numeros)
            # Adiciona o novo número ao resultado
            resultado.append(numeros[nova_posicao])
        else:
            # Mantém caracteres que não são letras ou números inalterados
            resultado.append(char)
    
    return ''.join(resultado)  # Junta a lista de resultados em uma string

# Função para descriptografar a mensagem
def descriptografar(mensagem, chave):
    resultado = []  # Lista para armazenar o resultado descriptografado
    
    # Percorre cada caractere da mensagem
    for char in mensagem:
        if char.lower() in alfabeto:  # Verifica se o caractere é uma letra
            # Pega a posição da letra no alfabeto
            posicao = alfabeto.index(char.lower())
            # Calcula a nova posição voltando o deslocamento
            nova_posicao = (posicao - int(chave)) % len(alfabeto)
            # Adiciona a nova letra ao resultado, mantendo maiúscula/minúscula
            if char.isupper():
                resultado.append(alfabeto[nova_posicao].upper())
            else:
                resultado.append(alfabeto[nova_posicao])
        elif char in numeros:  # Verifica se o caractere é um número
            # Pega a posição do número
            posicao = numeros.index(char)
            # Calcula a nova posição voltando o deslocamento
            nova_posicao = (posicao - int(chave)) % len(numeros)
            # Adiciona o novo número ao resultado
            resultado.append(numeros[nova_posicao])
        else:
            # Mantém caracteres que não são letras ou números inalterados
            resultado.append(char)
    
    return ''.join(resultado)  # Junta a lista de resultados em uma string

# Função que lida com a visualização e processamento dos dados
def criptografia_view(request):
    resultado = None

    if request.method == 'POST':
        form = CriptografiaForm(request.POST)
        
        if form.is_valid():
            mensagem = form.cleaned_data['mensagem']
            chave = form.cleaned_data['chave']
            acao = form.cleaned_data['acao']
            if acao == 'criptografar':
                resultado = criptografar(mensagem, chave)
            elif acao == 'descriptografar':
                resultado = descriptografar(mensagem, chave)
    else:
        form = CriptografiaForm()
    return render(request, 'criptografia_form.html', {'form': form, 'resultado': resultado})