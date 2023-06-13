import pytest
from lib.password_checker import *

#checking long password with letters and numbers
def test_valid_password():
    new_password = PasswordChecker()
    assert new_password.check("Password1234")

#checking short password
def test_invalid_password():
    new_password = PasswordChecker()
    with pytest.raises(Exception) as e: # <-- New code
        new_password.check("1234")
    error_message = str(e.value) # <-- New code
    assert error_message == "Invalid password, must be 8+ characters."

#chekc password of numbers
def test_password_of_numbers():
    new_password = PasswordChecker()
    with pytest.raises(Exception) as e: # <-- New code
        new_password.check(34567898765456)
    error_message = str(e.value) # <-- New code
    assert error_message == "Invalid type of pasword, must be string"
