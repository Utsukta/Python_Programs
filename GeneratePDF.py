
from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=25)

# create a cell
pdf.cell(200, 10, txt="Hello World!", ln=1, align='C')

pdf.output("info.pdf")

from pypdf import PdfReader

reader = PdfReader("info.pdf")

print(len(reader.pages))

