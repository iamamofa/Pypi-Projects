#Need the library -- use ==> pip install pdf2docx (to install the various libraries for use)

from pdfdocx import Converter

pdf_file = 'calculatiing.pdf'

docx_file = 'sammple.docx'

cv = Converter(pdf_file)
cv.converter(docx_file)
cv.close()

