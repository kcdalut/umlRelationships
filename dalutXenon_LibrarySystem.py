class Publication:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def get_title(self):
        return self.title
    
    def get_author(self):
        return self.author()

    def set_title(self, title):
        self.title = title

    def set_author(self, author):
        self.author = author

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")

class Book(Publication):
    def __init__(self, title: str, author: str, number_of_pages: int):
        super().__init__(title, author)
        self.__number_of_pages = number_of_pages

    def get_number_of_pages(self):
        return self.__number_of_pages

    def set_number_of_pages(self, number_pages):
        if number_pages > 0:
            self.__number_of_pages = number_pages
        else:
            print(f"Please ensure that the number of pages is positive.")
            
class Magazine(Publication):
    def __init__(self, title: str, author: str, issue_number: int):
        super().__init__(title, author)
        self.__issue_number = issue_number

    def get_issue_number(self):
        return self.__issue_number

    def set_issue_number(self, issue_number):
        if issue_number > 0:
            self.__issue_number = issue_number
        else:
            print(f"Please ensure that the issue number is positive.")

pub1 = Publication("Journal of Experimental Psychology", "Ratchiff, R. & Van Dongen, H.")
book1= Book("The Hobbit", "J.R.R. Tolkien", 310)
mag1 = Magazine ("National Geographic", "Various Authors", 202)

print("Publication Information:")
pub1.display_info()

print("\nBook Information:")
book1.set_number_of_pages (-310) 
book1.display_info()
print(book1.get_number_of_pages())

print("\nMagazine Information:")
mag1.display_info()
print(mag1.get_issue_number())
