from mock import Mock
from firstclasspostcodes.errors import ResponseError


class TestResponseErrorClass:
    def test_api_error_instantiation(self):
        response = {'docUrl': 'example.com', 'type': 'some-type', 'message': 'message'}
        error = ResponseError(**response)
        assert str(error) == 'message'
        assert error.type == 'some-type'
        assert error.doc_url == 'example.com'

    def test_client_error_instantiation(self):
        error = ResponseError('some message', type='client-error')
        assert str(error) == 'some message'
        assert error.type == 'client-error'
        assert len(error.doc_url) > 0
        assert 'client-error' in error.doc_url
