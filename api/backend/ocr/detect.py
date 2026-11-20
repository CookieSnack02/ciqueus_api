from api.backend.analysis import type_file # Identifica o tipo de arquivo
from api.backend.ocr.pdf import pdf_detect # Processa PDFs
from api.backend.ocr.images import image_detect # Processa imagens


def processar_arquivo():
    # Pergunta o caminho UMA vez e delega para o detector certo
    tipo_arquivo, caminho = type_file.identificacao_arquivo()

    if tipo_arquivo == 'PDF':
        return pdf_detect.extracao_texto_questao_pdf(caminho)
    elif tipo_arquivo == 'IMAGEM':
        return image_detect.extracao_texto_questao_imagem(caminho)
    else:
        print("O arquivo não é um PDF nem uma imagem. Não é possível processar o arquivo.")
        return None


if __name__ == "__main__":
    texto = processar_arquivo()
    if texto:
        print(texto)
