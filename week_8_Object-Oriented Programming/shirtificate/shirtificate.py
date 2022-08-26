from unicodedata import name
from fpdf import FPDF


def main():
    name = "John Harvard"

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.set_auto_page_break(False)
    pdf.add_page()
    
    pdf.set_font("arial", "B", 48)
    pdf.cell(200, 50, 'CS50 Shirtificate', new_x="LMARGIN", new_y="NEXT", align='C')
    
    pdf.image("shirtificate.png", w=pdf.epw)   

    pdf.set_font_size(30)
    pdf.set_text_color(255, 255, 255)
    pdf.text(45, y=120, txt=f"{name} took CS50")

    # Calculating width of title and setting cursor position:
    pdf.output("shirtificate.pdf")


if __name__=="__main__":
    main()