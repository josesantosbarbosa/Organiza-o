"""
Organizador de Arquivos (versão simples)
------------------------------------------
Este script organiza os arquivos de uma pasta em subpastas,
de acordo com o tipo de cada arquivo.

Exemplo: "foto.jpg" vai para a pasta "Imagens".
         "relatorio.pdf" vai para a pasta "Documentos".
"""

import os
import shutil

# Dicionário
CATEGORIAS = {
    "Imagens": [".jpg", ".jpeg", ".png"],
    "Documentos": [".pdf", ".docx", ".txt"],
    "Planilhas": [".xlsx", ".csv"],
}


pasta = input("Digite o caminho da pasta: ").strip()

# lista os arquivos
for nome_arquivo in os.listdir(pasta):
    caminho_arquivo = os.path.join(pasta, nome_arquivo)

    # Ignora subpastas, só mexe em arquivos
    if os.path.isdir(caminho_arquivo):
        continue

    # splita e converte a extenção para minusculo
    extensao = os.path.splitext(nome_arquivo)[1].lower()

    
    categoria_encontrada = "Outros"
    for categoria, extensoes in CATEGORIAS.items():
        if extensao in extensoes:
            categoria_encontrada = categoria
            break

    # Cria a subpasta da categoria, se ainda não existir
    pasta_destino = os.path.join(pasta, categoria_encontrada)
    os.makedirs(pasta_destino, exist_ok=True)

    # Move
    shutil.move(caminho_arquivo, os.path.join(pasta_destino, nome_arquivo))
    print(f"{nome_arquivo} -> {categoria_encontrada}/")

print("Organização concluída!")
