from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 24)
        self.cell(0, 10, "CS50 Shirtificate", 0, 1, "C")

    def add_shirtificate(self, name):
        # Add the image to the PDF
        self.image("shirtificate.png", x=0, y=60, w=210)

        # Add the name text
        self.set_xy(0, 140)
        self.set_font("Arial", "B", 36)
        self.set_text_color(255, 255, 255)
        self.cell(210, 10, f"{name} took CS50", 0, 1, "C")

def main():
    name = input("Name: ")
    pdf = PDF()
    pdf.add_page()
    pdf.add_shirtificate(name)
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
