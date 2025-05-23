from fpdf import FPDF

def main():
    name = input("Name: ")

    pdf = FPDF()
    pdf.add_page()

    pdf.image("shirtificate.png", x=0, y=0, w=210, h=297)

    pdf.set_font("Helvetica", "B", 24)
    pdf.set_text_color(255, 255, 255)  # white
    pdf.set_xy(0, 150)  # position vertically on shirt
    pdf.cell(210, 10, f"{name} took CS50", align="C")  # centered horizontally

    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
