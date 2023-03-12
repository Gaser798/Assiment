class user:
    def __int__(self,name,id,email):
        self.name = name
        self.id = id
        self.email = email

    def search_for_Book(self):
        pass

class Normal_User(user):
    def __int__(self, normal_user_name,normal_user_id,normal_user_email):
        super().__int__(normal_user_name,normal_user_id,normal_user_email)

    def Borrow_Book(self):
        pass
    def Return_Book(self):
        pass
    def Extend_loan_period_for_a_b(self):
        pass


class librarian(user):
    def __int__(self, librarian_user_name,librarian_user_id,librarian_user_email):
        super().__int__(librarian_user_name,librarian_user_id,librarian_user_email)

    def Add_Book(self):
        pass
    def Remove_Book(self):
        pass