import pytest
from textaugment import back_Translation, synonym_Replacement


@pytest.fixture(scope='module')
def sample_text():
    return "The quick brown fox jumps over the lazy dog."


def test_back_Translation(sample_text):
    augmented_texts = back_Translation(sample_text)
    assert isinstance(augmented_texts, list)
    assert len(augmented_texts) > 0


def test_synonym_Replacement(sample_text):
    augmented_text = synonym_Replacement(sample_text)
    assert isinstance(augmented_text, str)
    assert augmented_text != sample_text
