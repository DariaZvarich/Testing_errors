import pytest
from lib.present import Present

def test_wraping_a_present():
    present = Present()
    present.wrap(" flowers")
    result = present.unwrap()
    assert result == " flowers" 

def test_wraping_multiple_items():
    present = Present()
    present.wrap(" flowers")
    with pytest.raises(Exception) as e: # <-- New code
        present.wrap(" socks")
    error_message = str(e.value) # <-- New code
    assert error_message == "A contents has already been wrapped."

def test_unwrap_empty_present():
    present = Present()
    with pytest.raises(Exception) as e: # <-- New code
        present.unwrap()
    error_message = str(e.value) # <-- New code
    assert error_message == "No contents have been wrapped."

def test_wraping_a_number():
    present = Present()
    present.wrap(3)
    result = present.unwrap()
    assert result == 3