import os
import random
import requests
from urllib.parse import urlparse
from firstclasspostcodes import Client
from firstclasspostcodes.configuration import Configuration

API_URL = os.environ.get('API_URL')

URL = urlparse(API_URL)

KEY = os.environ.get('API_KEY')

configuration = {'protocol': URL.scheme, 'host': URL.netloc, 'base_path': URL.path, 'api_key': KEY}


class TestIntegrationClientClass:
    def setup_method(self):
        self.postcodes = requests.get(f'{API_URL}/data/.postcodes').json()

    def test_get_postcode_responds_correctly(self):
        postcode = random.choice(self.postcodes)['postcode']
        client = Client(**configuration)
        response = client.get_postcode(postcode=postcode)
        assert response['postcode'] == postcode

    def test_get_lookup_responds_correctly(self):
        location = random.choice(self.postcodes)
        postcode = location['postcode']
        latitude = location['latitude']
        longitude = location['longitude']
        client = Client(**configuration)
        response = client.get_lookup(latitude=latitude, longitude=longitude)
        assert response[0]['postcode'] == postcode
