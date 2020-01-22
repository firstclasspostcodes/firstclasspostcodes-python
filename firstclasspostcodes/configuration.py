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

    def __init__(self, **config):
        for key, value in config.items():
            setattr(self, key, value)

    def base_url(self):
        base_path = PurePath('/', self.base_path)
        return '{}://{}{}'.format(self.protocol, self.host, base_path)

    def request_params(self):
        params = {
            'timeout': self.timeout,
            'verify': self.ssl_verify,
            'headers': {
                'x-api-key': self.api_key,
                'accept': 'application/#{}; q=1.0, application/json; q=0.5'.format(self.content)
            }
        }

        if self.cert_file:
            params['cert'] = self.cert_file

        return params
