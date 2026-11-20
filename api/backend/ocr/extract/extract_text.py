import pymupdf


def extract_text_from_pdf(pdf_path):
    # Abrir o arquivo PDF usando o PyMuPDF
    textos = []
    with pymupdf.open(pdf_path) as doc:
        for page in doc:
            # page.get_text() devolve UMA string com todo o texto da página
            textos.append(page.get_text())

    # Junta o texto de todas as páginas, separado por quebra de linha
    return "\n".join(textos)


# Conversor do marker-pdf guardado em cache: carregar os modelos é lento
# (segundos + GBs de RAM), então só carregamos uma vez.
_converter = None


def extract_text_from_image(image_path):
    # Imports aqui dentro para que quem só usa PDF não precise do marker/PyTorch
    from marker.converters.pdf import PdfConverter
    from marker.models import create_model_dict
    from marker.output import text_from_rendered

    # Feito para que conversor dseja carregado se ele for vazio
    global _converter
    if _converter is None:
        _converter = PdfConverter(artifact_dict=create_model_dict())

    # O marker aceita imagens como entrada; o texto retornado vem em Markdown
    rendered = _converter(str(image_path))
    texto, _, _ = text_from_rendered(rendered)
    return texto
