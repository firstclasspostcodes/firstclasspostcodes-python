def parse_float(val):
    try:
        number = float(val)
    except ValueError:
        return False
    else:
        return number


def within(latitude, longitude):
    return -90 <= latitude <= 90 and -180 <= longitude <= 180


class GetLookup:
    def get_lookup(self, params={}):
        error_object = None

        if type(params) is not dict:
            raise ValueError(f'Expected dict, received: {type(params)}')

        if 'latitude' not in params or 'longitude' not in params:
            error_object = {
                'message': 'Missing required parameters, expected { latitude, longitude }',
                'docUrl': 'https://docs.firstclasspostcodes.com/operation/getLookup'
            }

        latitude = parse_float(params['latitude'])
        longitude = parse_float(params['longitude'])
        radius = parse_float(params['radius']) or 0.1

        query_params = {
            'latitude': latitude,
            'longitude': longitude,
            'radius': radius,
        }

        if latitude is False or longitude is False:
            error_object = {
                'message': f'Parameter is invalid: {query_params}',
                'docUrl': 'https://docs.firstclasspostcodes.com/operation/getLookup'
            }

        request_params = {
            'method': 'get',
            'path': '/lookup',
            'query_params': query_params,
        }

        self.configuration.logger.debug('Executing operation getLookup: %s', request_params)

        self.emit('operation:getLookup', request_params)

        if error_object:
            error = ParameterValidationError(error_object)
            self.configuration.logger.error('Encountered ParameterValidationError: %s', error)
            self.emit('error', error)
            raise error

        response = self.request(request_params)

        return response
