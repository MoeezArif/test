

import pytest
from .main import parse_comp1


@pytest.mark.parametrize("str_value",['parse','copy'])
def test_commands(data, str_value , expected):
    command_list = parse_comp1(data, str_value)
    assert command_list == expected , 'Not Equal'
