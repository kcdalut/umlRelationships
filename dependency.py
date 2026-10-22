class Document:
  def __init__(self, title: str, content: str):
    self.title = title
    self.content = content


class Printer:
  def print_document(self, document: Document):
    print(document.title)
    print(document.content)


my_document = Document("Report", "Annual sales data")
my_printer = Printer()

my_printer.print_document(my_document)
