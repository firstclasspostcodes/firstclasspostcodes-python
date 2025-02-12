from firstclasspostcodes.errors import ParameterValidationError


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
    def get_lookup(self, latitude, longitude, radius=0.1):
        error_object = None

        parsed_latitude = parse_float(latitude)
        parsed_longitude = parse_float(longitude)
        parsed_radius = parse_float(radius) or 0.1

        query_params = {
            'latitude': parsed_latitude,
            'longitude': parsed_longitude,
            'radius': parsed_radius,
        }

        is_valid_coordinate = within(parsed_latitude, parsed_longitude)

        if parsed_latitude is False or parsed_longitude is False or is_valid_coordinate is False:
            error_object = {
                'message': 'Parameter is invalid: {}'.format(query_params),
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
            error = ParameterValidationError(**error_object)
            self.configuration.logger.error('Encountered: %s', error)
            self.emit('error', error)
            raise error

        response = self.request(**request_params)

        return response
