from firstclasspostcodes.configuration import Configuration

class TestConfigurationClass:
    def setup_method(self):
        self.foo = 'bar'

    def test_one(self):
        assert self.foo == "bar"

    # def test_two(self):
    #     x = "hello"
    #     assert hasattr(x, "check")