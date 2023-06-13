class PasswordChecker:
    def check(self, password):
        if type(password) is not str:
            raise Exception("Invalid type of pasword, must be string")
        if len(password) >= 8:
            return True
        else:
            raise Exception("Invalid password, must be 8+ characters.")