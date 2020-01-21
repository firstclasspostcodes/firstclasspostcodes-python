import re
import json
import requests
from firstclasspostcodes.response_error import ResponseError
from firstclasspostcodes.configuration import Configuration
from firstclasspostcodes.events import Events
from firstclasspostcodes.operations import Operations
from firstclasspostcodes.version import VERSION


class Client(Events, Operations):
    configuration = None

    user_agent = f'Firstclasspostcodes/python@{VERSION}'

    def __init__(self, configuration_overrides={}):
        super().__init__()
        self.configuration = Configuration(configuration_overrides)
        self.on("request", lambda req: self.configuration.logger.debug('Request: %s', req))
        self.on("response", lambda res: self.configuration.logger.debug('Request: %s', res))
        self.on("error", lambda err: self.configuration.logger.error(err))

    def request(self, options={}):
        url = self.build_request_url(options['path'])
        request_params = {'params': options['query_params']}.update(self.configuration.request_params())
        self.emit('request', {'url': url}.update(request_params))
        response = self.call_request(url, options['method'], request_params)
        data = response.json()
        self.emit('response', data)
        return data

    def call_request(self, url, method, params={}):
        try:
            request = getattr(requests, method)
            response = request(url, *params)
            if response.status_code == requests.codes.ok:
                return response
            try:
                raise ResponseError(response.json())
            except json.decoder.JSONDecodeError:
                raise ResponseError(response, 'network-error')
        except requests.exceptions.Timeout:
            raise ResponseError('Connection timed out', 'timeout')
        except requests.exceptions.RequestException as e:
            raise ResponseError(e, 'liberror')

    def build_request_url(self, path):
        url_path = re.sub(r"^\/", '', path)
        return f'{self.configuration.base_url()}/{url_path}'
