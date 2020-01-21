DOC_URL = "https://docs.firstclasspostcodes.com/ruby/errors"


class ResponseError(Exception):
    doc_url = None

    type = None

    def __init__(self, error, type=None):
        if type(error) is dict:
            super().__init__(error['message'])
            self.doc_url = error['docUrl']
            self.type = error['type']
            return
        super().__init__(error)
        self.doc_url = f'{DOC_URL}/{type}'
        self.type = type
