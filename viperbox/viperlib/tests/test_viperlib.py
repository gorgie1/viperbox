import os
import pytest
from .. import *

this_dir = os.path.dirname(__file__)

def test_dir_get():
    from .. import tests as parent
    # test for this module's directory
    assert dir_get(__file__) == this_dir
    # test for this module's parent's directory
    assert dir_get(os.path.dirname(parent.__file__)) == dir_get(this_dir)

def test_parent_module_name_get():
    assert parent_module_name_get() == 'viperbox'
    assert parent_module_name_get('root.whatever.whichever') == 'root.whatever'
    assert parent_module_name_get('') == ''
    with pytest.raises(ValueError):
        parent_module_name_get('aaa bbb')

def test_strdigit_normalize():
    assert strdigit_normalize('00')  == '00'
    assert strdigit_normalize('0')   == '00'
    assert strdigit_normalize('1')   == '01'
    assert strdigit_normalize('9')   == '09'
    assert strdigit_normalize('10')  == '10'
    assert strdigit_normalize('11')  == '11'
    assert strdigit_normalize('99')  == '99'
    assert strdigit_normalize('100') == '100'
    with pytest.raises(AssertionError):
        strdigit_normalize(0)
    with pytest.raises(AssertionError):
        strdigit_normalize(5)
    with pytest.raises(AssertionError):
        strdigit_normalize(9)
    with pytest.raises(AssertionError):
        strdigit_normalize(0.1)
    with pytest.raises(AssertionError):
        strdigit_normalize(1.1)
    with pytest.raises(AssertionError):
        strdigit_normalize(-1)
    with pytest.raises(AssertionError):
        strdigit_normalize('-1')
    with pytest.raises(AssertionError):
        strdigit_normalize('-11')
