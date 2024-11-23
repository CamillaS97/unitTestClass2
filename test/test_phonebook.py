from src.phonebook import Phonebook


class TestPhonebook:

    def test_add_success(self):
        expected_result = 'Numero adicionado'
        phonebook = Phonebook()
        result = phonebook.add('SAMU', '192')
        assert result == expected_result

    # Return message has a misstype
    def test_add_invalid_name_at(self):
        expected_result = 'Nome invalido'
        phonebook = Phonebook()
        result = phonebook.add('S@MU', '192')
        assert result == expected_result

    # Return message has a misstype
    def test_add_invalid_name_dollar(self):
        expected_result = 'Nome invalido'
        phonebook = Phonebook()
        result = phonebook.add('$AMU', '192')
        assert result == expected_result

    # should not be able to add letters to phone number
    def test_add_invalid_number(self):
        expected_result = 'Numero invalido'
        phonebook = Phonebook()
        result = phonebook.add('SAMU', 'Number')
        assert result == expected_result

    # Should not add empty number, but adds anyway since len = 0 and not < 0
    def test_add_empty_number(self):
        expected_result = 'Numero invalido'
        phonebook = Phonebook()
        result = phonebook.add('SAMU', '')
        assert result == expected_result

    def test_delete_from_phonebook(self):
        expected_result = 'Numero deletado'
        phonebook = Phonebook()
        phonebook.add('CTTU', '123')
        result = phonebook.delete('CTTU')
        assert result == expected_result

    def test_search_phonebook(self):
        expected_result = [{'192', 'SAMU'}]
        phonebook = Phonebook()
        phonebook.add('SAMU', '192')
        phonebook.add('CTTU', '123')
        result = phonebook.search('SAMU')
        assert result == expected_result

    def test_lookup_phonebook(self):
        expected_result = '192'
        phonebook = Phonebook()
        phonebook.add('SAMU', '192')
        phonebook.add('CTTU', '123')
        result = phonebook.lookup('SAMU')
        assert result == expected_result

