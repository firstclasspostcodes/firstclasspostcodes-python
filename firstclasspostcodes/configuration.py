import logging


class Configuration:
    api_key = None

    host = "api.firstclasspostcodes.com"

    content = "json"

    protocol = "https"

    base_path = "/data"

    logger = logging.getLogger("firstclasspostcodes")

    debug = False

    timeout = 30

    def __init__(self, options={}):
        for key in options.keys():
            setattr(self, key, options[key])
