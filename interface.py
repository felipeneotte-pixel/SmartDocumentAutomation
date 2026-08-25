import customtkinter as ctk
from tkinter import filedialog
import threading

from file_manager import FileManager
from pdf_reader import PDFReader
from logger import logger

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class SmartAutomationApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Smart Document Automation")

        self.geometry("900x600")

        self.resizable(False, False)

        self.folder = ""

        self.manager = FileManager()
        self.reader = PDFReader()

        self.create_widgets()

    def create_widgets(self):

        self.titleLabel = ctk.CTkLabel(
            self,
            text="Smart Document Automation",
            font=("Arial", 28, "bold")
        )

        self.titleLabel.pack(pady=20)

        self.selectButton = ctk.CTkButton(
            self,
            text="📂 Selecionar Pasta",
            command=self.select_folder,
            width=250,
            height=40
        )

        self.selectButton.pack(pady=10)

        self.folderLabel = ctk.CTkLabel(
            self,
            text="Nenhuma pasta selecionada."
        )

        self.folderLabel.pack()

        self.processButton = ctk.CTkButton(
            self,
            text="▶ Processar PDFs",
            command=self.start_process,
            width=250,
            height=40
        )

        self.processButton.pack(pady=20)

        self.progress = ctk.CTkProgressBar(self)

        self.progress.pack(fill="x", padx=40)

        self.progress.set(0)

        self.logBox = ctk.CTkTextbox(
            self,
            width=800,
            height=280
        )

        self.logBox.pack(pady=20)

    def select_folder(self):

        folder = filedialog.askdirectory()

        if folder:

            self.folder = folder

            self.folderLabel.configure(text=folder)

    def log(self, message):

        self.logBox.insert("end", message + "\n")

        self.logBox.see("end")

    def start_process(self):

        thread = threading.Thread(target=self.process)

        thread.start()

    def process(self):

        if self.folder == "":

            self.log("Selecione uma pasta primeiro.")

            return

        pdfs = self.manager.get_all_pdfs(self.folder)

        total = len(pdfs)

        if total == 0:

            self.log("Nenhum PDF encontrado.")

            return

        for index, pdf in enumerate(pdfs):

            logger.info(pdf.name)

            text = self.reader.extract_text(pdf)

            self.log(f"✔ {pdf.name}")

            self.log(text[:250])

            self.log("----------------------------------------")

            self.progress.set((index + 1) / total)

        self.log("")

        self.log("Processamento concluído!")
