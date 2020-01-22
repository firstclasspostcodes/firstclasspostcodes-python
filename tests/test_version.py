import re
from firstclasspostcodes.version import VERSION


class TestVersonClass:
    def test_it_exports_a_valid_version_number(self):
        assert re.match('^[0-9]+.[0-9]+.[0-9]+$', VERSION)