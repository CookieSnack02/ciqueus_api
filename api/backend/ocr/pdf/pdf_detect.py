from api.backend.ocr.extract.extract_text import extract_text_from_pdf # Função de extração de texto do PDF


def extracao_texto_questao_pdf(pdf_path):
    # Só processa PDF. Quem decide o tipo do arquivo é o dispatcher (api/backend/ocr/detect.py)
    print("Está sendo iniciado o processo de captura de texto do PDF.")
    return extract_text_from_pdf(pdf_path)
