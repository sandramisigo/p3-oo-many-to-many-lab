class Author:
    all_authors = []

    def __init__(self, name):
        if not isinstance(name, str) or not name:
            raise Exception('Name must be a non empty string')
        self.name = name
        self._contracts= []
        Author.all_authors.append(self)

    def contracts(self):
        """Returns a list of related contracts for the author."""
        return self._contracts
    
    def books(self):
        """Returns a list of books associated with the author's contracts."""
        return [contract.book for contract in self.contracts()]
    
    def sign_contract(self, book, date, royalties): 
        """Creates and returns a new Contract object between the author and the specified book with the specified date and royalties."""
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of the Book class.")
        new_contract = Contract(self, book, date, royalties)
        self._contracts.append(new_contract)
        return new_contract

    def total_royalties(self):
        """Calculates the total royalties earned from all contracts."""
        return sum(contract.royalties for contract in self._contracts)

        

class Book:
    all_books = []

    def __init__(self, title):

        if not isinstance(title, str)or not title:
            raise Exception('Title must be a non empty string')
        self.title = title
        Book.all_books.append(self)

    def contracts(self):
        """Returns a list of related contracts for the book."""
        return [contract for contract in Contract.all_contracts if contract.book == self]

    def authors(self):
        """Returns a list of authors associated with the book's contracts."""
        return [contract.author for contract in self.contracts()]



class Contract:
    all_contracts = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Author must be an instance of the Author class.")
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of the Book class.")
        if not isinstance(date, str) or not date:
            raise Exception("Date must be a non-empty string.")
        if not isinstance(royalties, int) or royalties < 0:
            raise Exception("Royalties must be a positive integer.")
        
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all_contracts.append(self)

        author._contracts.append(self)  # Ensures contracts are properly linked to the author
    
    @classmethod
    def contracts_by_date(cls, date):
        """Returns all contracts that have the same date as the date passed into the method."""
        return [contract for contract in cls.all_contracts if contract.date == date]





