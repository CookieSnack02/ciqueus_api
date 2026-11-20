# Deteccao do tipo de arquivo


import mimetypes # Tem como utilizar tambem o python-magic
from pathlib import Path # Localizacao do Arquivo


def identificacao_arquivo():
    """Pede o caminho ao usuario e retorna (tipo_arquivo, caminho_arquivo).

    tipo_arquivo: 'PDF', 'IMAGEM' ou None.
    """
    arquivo = input("Digite o caminho do arquivo: ").strip().strip('"') # Usuario digita o caminho
    caminho_arquivo = Path(arquivo) # caminho do arquivo

    if not caminho_arquivo.is_file():
        print("Arquivo não encontrado.")
        return None, caminho_arquivo

    mime = mimetypes.guess_type(caminho_arquivo)[0]
    tipo_arquivo = None

    if mime == 'application/pdf':
        tipo_arquivo = 'PDF'
        print("O arquivo é um PDF.")
    elif mime and mime.startswith('image/'):
        tipo_arquivo = 'IMAGEM'
        print("O arquivo é uma imagem.")

    return tipo_arquivo, caminho_arquivo
