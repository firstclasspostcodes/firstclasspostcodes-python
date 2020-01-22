DOC_URL = "https://docs.firstclasspostcodes.com/python/errors"


class ResponseError(Exception):
    doc_url = None

    type = None

    def __init__(self, message, type, docUrl=''):
        super().__init__(message)
        if len(docUrl) > 0:
            self.doc_url = docUrl
        else:
            self.doc_url = f'{DOC_URL}/{type}'
        self.type = type


class ParameterValidationError(ResponseError, Exception):
    def __init__(self, **error):
        super().__init__(type='parameter-validation-error', **error)
