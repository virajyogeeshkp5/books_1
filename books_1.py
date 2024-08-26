class books:
    def __init__(self, title, cost):
        self.title = title
        self.cost = cost
    def greet(self):
        print("Title of the book is:", self.title)

python_book = books("Learn and practice python programming", 55)
print(python_book.title)
print(python_book.cost)
python_book.greet()