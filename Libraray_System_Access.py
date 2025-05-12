class Member:
    def __init__(self, name, memberid):
        self.name = name
        self.memberid = memberid

    def display(self):
        print(f"Name: {self.name}")
        print(f"Membership ID: {self.memberid}")

class StudentMember(Member):
    def __init__(self, name, memberid):
        super().__init__(name, memberid)
        self.borrowed_books=0

    def add_book(self):
        self.borrowed_books+=1
        print("Book Checked Out Successfully")

    def return_book(self):
        if self.borrowed_books > 0:
            self.borrowed_books-=1
            print("Book returned Successfully")
        else:
            print("No Books remaining to return")
            
    def display_status(self):
        self.display()
        print(f"Books Currently Borrowed {self.borrowed_books}")


S1 = StudentMember("Nisarg Patel", "S070")
S1.display_status()
S1.add_book()
S1.display_status()
S1.return_book()
S1.display_status()
