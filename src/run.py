import pypdf
import os 


os.chdir('..')

import src.gai_interface as GI


## Set up GenAI connection
openai_key = open(r'openai_key.txt','r').read()

openAI = GI.GenAIconnector(openai_key)

#openAI.OpenAIconnect('say helooooo')


import src.pdf_reader as PR

### Read in PDF
file = r'data\apple10k_2023.pdf'
pages_with_tables = [25]

apple = PR.PDFReader(file)


page = pages_with_tables[0]
apple.tabula(page)