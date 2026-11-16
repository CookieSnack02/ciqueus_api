# Deteccao do tipo de arquivo 
import mimetypes # Tem como utilizar tambem o python-magic
from pathlib import Path # Localizacao do Arquivo

arquivo = input("Digite o caminho do arquivo: ").strip().strip('"') # Usuario digita o caminho
caminho_arquivo = Path(arquivo) # caminho do arquivo 


# Se for um arquivo de PDF 




# Se for um arquivo de imagem