import pypdf

class PDFReader:
    def __init__(self, file_path):
        
        self.pdf = pypdf.PdfReader(file_path)
        self.file_path = file_path
        self.num_pages = 0
        self.has_ocr_layer = False
        self.data_type = 'PDF'
        
    
    def page_details(self, page_no):

        page = self.pdf.get_page(page_no)

        hasOCR = True if page.extract_text() == True else False

        ### Has Table


        return {'OCR' : hasOCR}
    
    def get_metadata(self):
        self.num_pages = self.pdf_reader.get_num_pages()

        return {
            'number_of_pages': self.num_pages,
            'data_type': self.data_type,
            'has_ocr_layer': self.has_ocr_layer
        }
    

    def tabula(self, page):

        import tabula

        dfs = tabula(self.file_path, pages = page )

        return dfs





