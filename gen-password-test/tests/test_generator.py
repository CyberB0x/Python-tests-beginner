import pytest
import string
from my_pass.generator import generate_password

def test_length():
    pw = generate_password(10)
    assert len(pw) == 10


def test_characters():
    pw = generate_password(12)
    valid_chars = set(string.ascii_letters + string.digits)
    assert all(c in valid_chars for c in pw)


def test_min_length_error():
    with pytest.raises(ValueError):
        generate_password(3)

def test_uniqueness():
    password = {generate_password(8) for _ in range(100)}
    assert len(password) > 90