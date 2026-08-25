from pathlib import Path

from file_manager import FileManager
from pdf_reader import PDFReader
from logger import logger

def process():

    manager = FileManager()

    reader = PDFReader()

    folder = input("Informe a pasta dos PDFs: ")

    pdfs = manager.get_all_pdfs(folder)

    if not pdfs:

        print("Nenhum PDF encontrado.")
        return

    print(f"\n{len(pdfs)} PDFs encontrados.\n")

    for pdf in pdfs:

        logger.info(f"Lendo {pdf.name}")

        text = reader.extract_text(pdf)

        print("="*50)
        print(pdf.name)
        print("="*50)

        print(text[:500])

        print()

if __name__ == "__main__":

    process()
