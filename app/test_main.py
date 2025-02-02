from app.main import is_isogram


def test_is_isogram_true() -> None:
    assert is_isogram("playgrounds") is True


def test_is_isogram_false() -> None:
    assert is_isogram("look") is False


def test_is_isogram_case_insensitive() -> None:
    assert is_isogram("Adam") is False


def test_empty_string_is_isogram() -> None:
    assert is_isogram("") is True


def test_is_isogram_mixed_case() -> None:
    assert is_isogram("MixED") is True


def test_consecutive_letters_are_not_isogram() -> None:
    assert is_isogram("abba") is False


def test_non_consecutive_letters_are_not_isogram() -> None:
    assert is_isogram("hello") is False
