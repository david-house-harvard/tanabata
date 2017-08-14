"""
Common utils for project.
"""

def assert_has_width(br, element):
    """
    Helper function that checks element naturalWidth.
    """
    assert br.execute_script(
        "return (typeof arguments[0].naturalWidth!=\"undefined\" && arguments[0].naturalWidth > 0)",
        element
    ) is True
