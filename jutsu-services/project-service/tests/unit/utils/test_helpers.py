""" import pytest """
""" from src.utils.helpers import generate_name_key """


""" def test_generate_name_key_single_word(): """
"""     name = 'Project' """
"""     result = generate_name_key(name) """
"""     assert result == 'PRO', f"Expected 'PRO', but got {result}" """


""" def test_generate_name_key_multiple_words(): """
"""     name = 'Important Project' """
"""     result = generate_name_key(name) """
"""     assert result == 'IP', f"Expected 'IP', but got {result}" """


""" def test_generate_name_key_empty_string(): """
"""     name = '' """
"""     result = generate_name_key(name) """
"""     assert result == '', f"Expected '', but got {result}" """
