class User:
    def __init__(self, name, mail):
        self.name = name
        self.mail = mail

    def __str__(self):
     return self.name + " - " + self.mail