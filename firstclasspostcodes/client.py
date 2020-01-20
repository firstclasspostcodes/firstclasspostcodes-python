from firstclasspostcodes.configuration import Configuration
from firstclasspostcodes.events import Events
from firstclasspostcodes.operations import GetPostcode, GetLookup
from firstclasspostcodes.version import VERSION


class Client(Events, GetPostcode, GetLookup, object):
    configuration = None

    user_agent = f'Firstclasspostcodes/python@{VERSION}'

    def __init__(self, configuration_overrides={}):
        super().__init__()
        self.configuration = Configuration(configuration_overrides)
        self.on("request", lambda req: self.configuration.logger.debug('Request: %s', req))
        self.on("response", lambda res: self.configuration.logger.debug('Request: %s', res))
        self.on("error", lambda err: self.configuration.logger.error(err))
