from fpdf import FPDF

def pdf_format(name):
    pdf = FPDF()
    pdf.add_page()
    #Image: Add image
    pdf.image('shirtificate.png', w =pdf.epw, y=75)
    #Text: Title
    pdf.set_font('helvetica', size=50)
    pdf.cell(text="CS50 Shirtificate", h = 75, center=True, markdown=True)
    #Text: Add inputed Text
    pdf.set_font('helvetica', size=20)
    pdf.set_text_color(255,255,255)
    pdf.cell(text=f"{name} took CS50", h = 250, center=True, markdown=True)
    pdf.output("shirtificate.pdf")


def main():
    pdf_format(str(input("Name: ")))


if __name__ == "__main__":
    main()