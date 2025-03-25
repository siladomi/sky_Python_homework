import pytest
from string_utils import StringUtils

@pytest.fixture
def utils():
    return StringUtils()

class TestCapitalize:
    def test_capitalize_positive(self, utils):
        assert utils.capitalize("skypro") == "Skypro"
        assert utils.capitalize("hello world") == "Hello world"
        assert utils.capitalize("python") == "Python"

    def test_capitalize_empty_string(self, utils):
        assert utils.capitalize("") == ""

    def test_capitalize_already_capitalized(self, utils):
        assert utils.capitalize("Skypro") == "Skypro"

    def test_capitalize_with_numbers(self, utils):
        assert utils.capitalize("1skypro") == "1skypro"
        assert utils.capitalize("123") == "123"

class TestTrim:
    def test_trim_positive(self, utils):
        assert utils.trim("   skypro") == "skypro"
        assert utils.trim("  hello") == "hello"
        assert utils.trim(" \t\nhello") == "\t\nhello"  

    def test_trim_no_spaces(self, utils):
        assert utils.trim("skypro") == "skypro"

    def test_trim_empty_string(self, utils):
        assert utils.trim("") == ""

    def test_trim_multiple_spaces(self, utils):
        assert utils.trim("     skypro") == "skypro"

class TestContains:
    def test_contains_positive(self, utils):
        assert utils.contains("SkyPro", "S") is True
        assert utils.contains("SkyPro", "Pro") is True
        assert utils.contains("SkyPro", "y") is True

    def test_contains_negative(self, utils):
        assert utils.contains("SkyPro", "U") is False
        assert utils.contains("", "a") is False
        assert utils.contains("SkyPro", "sky") is False

    def test_contains_empty_string(self, utils):
        assert utils.contains("", "a") is False

    def test_contains_empty_symbol(self, utils):
        assert utils.contains("SkyPro", "") is True  

class TestDeleteSymbol:
    def test_delete_symbol_positive(self, utils):
        assert utils.delete_symbol("SkyPro", "k") == "SyPro"
        assert utils.delete_symbol("SkyPro", "Pro") == "Sky"
        assert utils.delete_symbol("HelloWorld", "o") == "HellWrld"

    def test_delete_symbol_not_found(self, utils):
        assert utils.delete_symbol("SkyPro", "X") == "SkyPro"

    def test_delete_symbol_empty_string(self, utils):
        assert utils.delete_symbol("", "a") == ""

    def test_delete_symbol_empty_symbol(self, utils):
        assert utils.delete_symbol("SkyPro", "") == "SkyPro"

    def test_delete_symbol_all_occurrences(self, utils):
        assert utils.delete_symbol("abababa", "a") == "bbb"

    def test_delete_symbol_whitespace(self, utils):
        assert utils.delete_symbol("a b c", " ") == "abc"