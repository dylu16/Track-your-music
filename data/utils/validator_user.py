import re

class ValidatorUser:
    def __init__(self, lastname, firstname, email, password, confirm_password):
        self.__lastname = lastname
        self.__firstname = firstname
        self.__email = email
        self.__password = password
        self.__confirm_password = confirm_password

    def validate_lastname(self):
        if len(self.__lastname) == 0:
            return False, "Câmpul nume nu poate fi gol"
        elif len(self.__lastname) < 3 or len(self.__lastname) > 20:
            return False, "Câmpul nume trebuie să conțină între 3 și 20 de caractere"
        elif not re.match("^[a-zA-Z]+$", self.__lastname):
            return False, "Câmpul nume trebuie să conțină doar litere"
        return True

    def validate_firstname(self):
        if len(self.__firstname) == 0:
            return (False, "Câmpul prenume nu poate fi gol")
        elif len(self.__firstname) < 3 or len(self.__firstname) > 20:
            return (False, "Câmpul prenume trebuie să conțină între 3 și 20 de caractere")
        elif not re.match("^[a-zA-Z]+$", self.__firstname):
            return (False, "Câmpul prenume trebuie să conțină doar litere")
        return True

    def validate_email(self):
        if len(self.__email) == 0:
            return (False, "Câmpul email nu poate fi gol")
        elif len(self.__email) > 50:
            return (False, "Câmpul email trebuie să conțină maxim 50 de caractere")
        elif '@' not in self.__email or '.' not in self.__email:
            return (False, "Câmpul email nu este valid")
        return True

    def validate_password(self):
        if len(self.__password) == 0:
            return (False, "Câmpul parola nu poate fi gol")
        elif len(self.__password) < 6 or len(self.__password) > 30:
            return (False, "Câmpul parola trebuie să conțină între 6 și 30 de caractere")
        elif not re.match("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{6,}$", self.__password):
            return (False, "Câmpul parola trebuie să conțină litere mici, mari și cifre")
        return True

    def validate_confirm_password(self):
        if len(self.__confirm_password) == 0:
            return (False, "Câmpul confirmare parola nu poate fi gol")
        elif len(self.__confirm_password) < 6 or len(self.__confirm_password) > 30:
            return (False, "Câmpul confirmare parola trebuie să conțină între 6 și 30 de caractere")
        elif not re.match("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{6,}$", self.__confirm_password):
            return (False, "Câmpul confirmare parola trebuie să conțină litere mici, mari și cifre")
        return True

    def validate_passwords(self):
        if self.__password != self.__confirm_password:
            return (False, "Câmpurile parola și confirmare parola nu sunt identice")
        return True

    def validate(self):
        result_validate_lastname = self.validate_lastname()
        result_validate_firstname = self.validate_firstname()
        result_validate_email = self.validate_email()
        result_validate_password = self.validate_password()
        result_validate_confirm_password = self.validate_confirm_password()
        result_validate_passwords = self.validate_passwords()

        if isinstance(result_validate_lastname, tuple):
            return result_validate_lastname
        if isinstance(result_validate_firstname, tuple):
            return result_validate_firstname
        if isinstance(result_validate_email, tuple):
            return result_validate_email
        if isinstance(result_validate_password, tuple):
            return result_validate_password
        if isinstance(result_validate_confirm_password, tuple):
            return result_validate_confirm_password
        if isinstance(result_validate_passwords, tuple):
            return result_validate_passwords
        return True
