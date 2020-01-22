from firstclasspostcodes.configuration import Configuration


class TestConfigurationClass:
    def test_base_url_works_correctly(self):
        config = Configuration(protocol='http', host='example.com', base_path='/test')
        assert config.base_url() == 'http://example.com/test'

    def test_request_params_works_correctly(self):
        config = Configuration(timeout=15, verify=False, api_key='test')
        request_params = config.request_params()
        assert type(request_params) is dict
        assert 'timeout' in request_params
        assert 'verify' in request_params
        assert 'headers' in request_params

    def configuration_key_is_not_empty(self, val):
        return type(val) is str and len(val) > 0

    def test_it_sets_keys_correctly(self):
        assert Configuration().api_key is None
        assert Configuration(api_key='test').api_key == 'test'

    def test_it_sets_host_correctly(self):
        assert self.configuration_key_is_not_empty(Configuration().host) is True

    def test_it_sets_content_correctly(self):
        assert self.configuration_key_is_not_empty(Configuration().content) is True

    def test_it_sets_protocol_correctly(self):
        assert self.configuration_key_is_not_empty(Configuration().protocol) is True

    def test_it_sets_base_path_correctly(self):
        assert self.configuration_key_is_not_empty(Configuration().base_path) is True
