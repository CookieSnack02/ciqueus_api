from api.backend.ocr.extract.extract_text import extract_text_from_image # Função de extração de texto da imagem


def extracao_texto_questao_imagem(image_path):
    # Só processa imagem. Quem decide o tipo do arquivo é o dispatcher (api/backend/ocr/detect.py)
    print("Está sendo iniciado o processo de captura de texto da imagem.")
    return extract_text_from_image(image_path)
