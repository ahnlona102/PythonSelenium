class User:
    def __init__(self, username="", domain="", password="", confirm_password="", passport="", arrive="", seat_type="", amount_ticket="", email="", depart_date="", depart="", date=0):
        self.username = username
        self.domain = domain
        self.password = password
        self.confirm_password = confirm_password
        self.passport = passport
        self.arrive = arrive
        self.seat_type = seat_type
        self.amount_ticket = amount_ticket
        self.email = email
        self.depart_date = depart_date
        self.depart = depart
        self.date = date

    def get_username(self):
        return self.username

    def set_username(self, username):
        self.username = username

    def get_domain(self):
        return self.domain

    def set_domain(self, domain):
        self.domain = domain

    def get_password(self):
        return self.password

    def set_password(self, password):
        self.password = password

    def get_confirm_password(self):
        return self.confirm_password

    def set_confirm_password(self, confirm_password):
        self.confirm_password = confirm_password

    def get_passport(self):
        return self.passport

    def set_passport(self, passport):
        self.passport = passport

    def get_arrive(self):
        return self.arrive

    def set_arrive(self, arrive):
        self.arrive = arrive

    def get_seat_type(self):
        return self.seat_type

    def set_seat_type(self, seat_type):
        self.seat_type = seat_type

    def get_amount_ticket(self):
        return self.amount_ticket

    def set_amount_ticket(self, amount_ticket):
        self.amount_ticket = amount_ticket

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_depart_date(self):
        return self.depart_date

    def set_depart_date(self, depart_date):
        self.depart_date = depart_date

    def get_depart(self):
        return self.depart

    def set_depart(self, depart):
        self.depart = depart

    def get_date(self):
        return self.date

    def set_date(self, date):
        self.date = date
