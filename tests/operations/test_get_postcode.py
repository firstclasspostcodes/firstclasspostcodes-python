import os
from urllib.parse import urlparse
from mock import Mock, ANY
from firstclasspostcodes.operations import GetPostcode
from firstclasspostcodes.configuration import Configuration

URL=urlparse(os.environ.get('API_URL'))

KEY=os.environ.get('API_KEY')


class GetPostcodeStub(GetPostcode):
    configuration = Configuration(protocol=URL.scheme, host=URL.netloc, base_path=URL.path, api_key=KEY)

    emit = Mock()

    request = Mock()


class TestGetPostcodeClass:
    def test_successful_call_to_get_postcode(self):
        postcode = 'w86gh'
        params = {'search': postcode}
        client = GetPostcodeStub()
        client.request = Mock(return_value=12345)
        response = client.get_postcode(postcode)
        client.emit.assert_called_once_with('operation:getPostcode', ANY)
        client.request.assert_called_once_with(method='get', path='/postcode', query_params=params)
        assert response == 12345
    