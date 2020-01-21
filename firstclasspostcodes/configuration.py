from pathlib import PurePath
import logging


class Configuration:
    api_key = None

    host = "api.firstclasspostcodes.com"

    content = "json"

    protocol = "https"

    base_path = "/data"

    logger = logging.getLogger("firstclasspostcodes")

    # True, False or path to CA Bundle file
    ssl_verify = True

    # None or a single file (containing the private key and
    # the certificate) or as a tuple of both files’ paths
    cert_file = None

    debug = False

    timeout = 30

    def __init__(self, options={}):
        for key in options.keys():
            setattr(self, key, options[key])

    def base_url(self):
        base_path = PurePath('/', self.base_path)
        return f'{self.protocol}://{self.host}{base_path}'

    def request_params(self):
        params = {
            'timeout': self.timeout,
            'verify': self.ssl_verify,
            'headers': {
                'x-api-key': self.api_key,
                'accept': f'application/#{self.content}; q=1.0, application/json; q=0.5'
            }
        }

        if self.cert_file:
            params['cert'] = self.cert_file

        return params
