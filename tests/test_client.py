import re
import json
import pytest
import requests
from mock import Mock, ANY
from firstclasspostcodes.version import VERSION
from firstclasspostcodes.configuration import Configuration
from firstclasspostcodes.client import Client
from firstclasspostcodes.errors import ResponseError


class TestClientClass:
    def test_get_postcode_is_included(self):
        assert "get_postcode" in dir(Client())

    def test_get_lookup_is_included(self):
        assert "get_lookup" in dir(Client())

    def test_user_agent_is_correct(self):
        client = Client()
        assert re.match('Firstclasspostcodes/python@{}'.format(VERSION), client.user_agent)

    def test_configuration_overrides_are_set_correctly(self):
        api_key = 'abdertyhgfde'
        client = Client(api_key=api_key)
        assert isinstance(client.configuration, Configuration)
        assert client.configuration.api_key == api_key

    def test_build_request_url_returns_correctly(self):
        client = Client(protocol='https', host='example.com', base_path='/test')
        assert client.build_request_url('/lookup') == 'https://example.com/test/lookup'

    def test_request_calls_correctly(self):
        client = Client(protocol='https', host='example.com', base_path='/test')
        response = Mock()
        response.json = Mock(return_value=12345)
        client.call_request = Mock(return_value=response)
        test_response = client.request(method='get', query_params={'a': 1}, path='/call')
        client.call_request.assert_called_once_with('https://example.com/test/call', 'get', ANY)
        response.json.assert_called_once()
        assert test_response == 12345

    def test_call_request_returns_correctly_on_ok(self):
        client = Client()
        mock_response = Mock(**{'status_code': 200})
        requests.get = Mock(return_value=mock_response)
        client.call_request(url='http://example.com', method='get')
        requests.get.assert_called_once_with('http://example.com')

    def test_call_request_raises_api_error(self):
        client = Client()
        json = {'docUrl': 'docUrl', 'message': 'error message', 'type': 'type'}
        mock_response = Mock(**{'status_code': 400, 'json.return_value': json})
        requests.get = Mock(return_value=mock_response)
        with pytest.raises(ResponseError) as error:
            client.call_request(url='http://example.com', method='get')
        assert str(error.value) == 'error message'
        assert error.value.type == 'type'
        assert error.value.doc_url == 'docUrl'

    def test_call_request_raises_json_decode_error(self):
        client = Client()
        json_error = json.decoder.JSONDecodeError(pos=0, doc='', msg='')
        response = {'content': 'error message', 'status_code': 500, 'json.side_effect': json_error}
        mock_response = Mock(**response)
        requests.get = Mock(return_value=mock_response)
        with pytest.raises(ResponseError) as error:
            client.call_request(url='http://example.com', method='get')
            assert str(error.value) == 'error message'
        assert error.value.type == 'network-error'
        assert 'network-error' in error.value.doc_url
