import pdfreader
from pdfreader import PDFDocument, SimplePDFViewer


def check_bank_statement_contains_entered_name(customer_entered_name: str):
    file_name = "example.pdf"
    fd = open(file_name, "rb")
    viewer = SimplePDFViewer(fd)

    viewer.render()
    output = viewer.canvas.strings
    print(output)

    return customer_entered_name in output

print(check_bank_statement_contains_entered_name("Ms Chiaki Mizuta"))
