from fpdf import FPDF

class Shirtificate(FPDF):
    def __init__(self, name):
        super().__init__(orientation="P", unit="mm", format="A4")
        self.name = name

    def create_shirtificate(self):
        # Set font and size
        self.set_font("Helvetica", "", 30)
        self.set_text_color(0, 0, 0)

        # Add "CS50 Shirtificate" text centered horizontally
        self.cell(0, 50, "CS50 Shirtificate", align="C", ln=True)

        # Add the shirt image centered horizontally
        self.image("shirtificate.png", x=0, y=45, w=self.w)

        # Add the user's name on top of the shirt in white text
        self.set_font("Helvetica", "", 20)
        self.set_text_color(255, 255, 255)
        self.text(x=55, y=125, txt=f"{self.name} took CS50")

        # Save the PDF
        self.output("shirtificate.pdf")

def main():
    name = input("Enter your name: ")
    shirtificate = Shirtificate(name)
    shirtificate.create_shirtificate()
    print("Shirtificate created successfully!")

if __name__ == "__main__":
    main()
