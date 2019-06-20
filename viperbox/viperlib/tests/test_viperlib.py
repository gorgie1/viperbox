
def test_dir_get():
    import os
    from .. import dir_get
    from .. import tests as parent
    this_dir = os.path.dirname(__file__)
    # test for this module directory
    assert dir_get(__file__) == this_dir
    # test for this module parent's directory
    assert dir_get(os.path.dirname(parent.__file__)) != dir_get(this_dir)
