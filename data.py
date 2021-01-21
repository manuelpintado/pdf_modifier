# -- ------------------------------------------------------------------------------------ -- #
# -- proyecto: Automatizar separacion de pdfs
# -- archivo: data.py - funciones para modificar pdfs
# -- mantiene: IF Manuel Pintado
# -- repositorio: https://github.com/manuelpintado/Proyecto_Equipo_6.git
# -- ------------------------------------------------------------------------------------ -- #


# Import libraries
import os
from PyPDF2 import PdfFileReader, PdfFileWriter
import pandas as pd


class Join_PDF(object):
    "class to join pdf files into a single one"

    def __init__(self, list_number: int,
                 location='C:/Users/manue/OneDrive - VANRENTA, S.A. DE C.V/FINANZAS/BURZATILIZACION/VRTCB20/ENDOSO PAGARES/DOCUMENTO ESCANEADO/separados/',
                 destination='C:/Users/manue/OneDrive - VANRENTA, S.A. DE C.V/FINANZAS/BURZATILIZACION/VRTCB20/ENDOSO PAGARES/DOCUMENTO ESCANEADO/'):
        self.list = list_number
        self.location = location
        self.destination = destination

    def join(self):
        os.chdir(self.location)  # Set os location
        pdf2merge = []  # Create empty list
        for filename in os.listdir('.'):  # Cicle through all files in directory
            if filename.endswith('.pdf'):
                pdf2merge.append(filename)  # Create list of files to merge

        pdfWriter = PdfFileWriter()  # Initialize new pdf
        # loop through all PDFs
        for filename in pdf2merge:  # Cycle through file list
            # rb for read binary
            pdfFileObj = open(filename, 'rb')
            pdfReader = PdfFileReader(pdfFileObj)
            # Opening each page of the PDF
            for pageNum in range(pdfReader.numPages):  # Merge all pages in each file
                pageObj = pdfReader.getPage(pageNum)
                pdfWriter.addPage(pageObj)
                # save PDF to file, wb for write binary
                pdfOutput = open(f'{self.destination}lista_{self.list}.pdf', 'wb')
            pdfFileObj.close()  # Close merged pdf
        # Outputting the PDF
        pdfWriter.write(pdfOutput)  # Output final pdf
        # Closing the PDF writer
        pdfOutput.close()  # Close new pdf


class Split_PDF(object):

    "class to split a big pdf file into individual pdfs according to list"

    def __init__(self, list_number: int, split_n: int):
        self.lista = list_number
        self.split_n = split_n

    def split(self):
        file_path = f'C:/Users/manue/OneDrive - VANRENTA, S.A. DE C.V/FINANZAS/BURZATILIZACION/VRTCB20/ENDOSO ' \
                    f'PAGARES/DOCUMENTO ESCANEADO/lista_{self.lista}.pdf '
        lists = pd.read_csv(
            'C:/Users/manue/OneDrive - VANRENTA, S.A. DE C.V/FINANZAS/BURZATILIZACION/VRTCB20/LISTAS PAGARES ENDOSADOS.csv')

        first_list = pd.DataFrame(lists[f'LIST_{self.lista}'].values).dropna()

        pdf = PdfFileReader(file_path)

        start_page = 0
        end_page = self.split_n

        for contract in first_list.values:
            pdfwriter = PdfFileWriter()
            for k in range(start_page, end_page):
                pdfwriter.addPage(pdf.getPage(k))
            contrato = str(contract).strip("['']")
            with open(f'C:/Users/manue/OneDrive - VANRENTA, S.A. DE C.V/FINANZAS/BURZATILIZACION/VRTCB20/ENDOSO '
                      f'PAGARES/PAGARES INDIVIDUALES/Endoso_{contrato}.pdf', 'wb') as f:
                pdfwriter.write(f)
                f.close()
            start_page += self.split_n
            end_page += self.split_n
