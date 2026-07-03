import pytest
from src.core import Core
@pytest.mark.parametrize("password",[
    "password",
    "password123",
    "qwerty",
    "admin123"]
    )

def test_common_passwords(password):
    analyzer = Core(password, "", "")
    analyzer.common_password()
    assert analyzer.used_common_password is True