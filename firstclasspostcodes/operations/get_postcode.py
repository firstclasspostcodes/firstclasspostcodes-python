from firstclasspostcodes.errors import ParameterValidationError


class GetPostcode:
    def get_postcode(self, postcode):
        error_object = None

        if type(postcode) != str or len(postcode) == 0:
            error_object = {
                'message': 'Unexpected postcode parameter: "{}"'.format(postcode),
                'docUrl': 'https://docs.firstclasspostcodes.com/operation/getPostcode',
            }

        request_params = {
            'method': 'get',
            'path': '/postcode',
            'query_params': {
                'search': postcode,
            },
        }

        self.configuration.logger.debug('Executing operation getPostcode: %s', request_params)

        self.emit('operation:getPostcode', request_params)

        if error_object:
            error = ParameterValidationError(**error_object)
            self.configuration.logger.error('Encountered: %s', error)
            self.emit('error', error)
            raise error

        response = self.request(**request_params)

        return response
