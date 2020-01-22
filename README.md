![Cover](/.github/images/cover.png)

# Firstclasspostcodes
The Firstclasspostcodes Python library provides convenient access to the Firstclasspostcodes API from applications written in the Python language. It includes pre-defined methods and helpers to help you easily integrate the library into any application.

The library also provides other features. For example:

* Easy configuration path for fast setup and use.
* Helpers for listing and formatting addresses.
* Built-in methods for easily interacting with the Firstclasspostcodes API.

## Documentation
See [Python API docs](https://docs.firstclasspostcodes.com/python/getting-started) for detailed usage and examples.

## Installation
You don't need this source code unless you want to modify the package. If you just want to use the package, just run:

```
pip install --upgrade stripe
```

Install from source with:

```
python setup.py install
```

## Requirements

* Python 3.5+ (PyPy supported)
* An API key from [https://firstclasspostcodes.com](https://firstclasspostcodes.com)

## Usage
The library needs to be configured with your API key, which is available on the [dashboard](https://dashboard.firstclasspostcodes.com).

```python
from firstclasspostcodes import Client

client = Client(api_key='3454tyrgdfsew23')

# retrieve a postcode
response = client.get_postcode('AB30 1FR')

print(response['postcode'])
```

## Configuration
The library can be configured with several options depending on the requirements of your setup:

```python
from firstclasspostcodes import Client

client = Client(
    # The API Key to be used when sending requests to the 
    # Firstclasspostcodes API
    api_key='3454tyrgdfsew23',

    # The host to send API requests to. This is typically changed
    # to use the mock service for testing purposes
    host="api.firstclasspostcodes.com",

    # The default content type is json, but can be changed to "geo+json"
    # to return responses as GeoJSON content type
    content = "json",

    # Typically, always HTTPS, but useful to change for testing
    # purposes
    protocol = "https",

    # The base path is "/data", but useful to change for testing
    # purposes
    base_path = "/data",

    # The default request timeout for the library.
    timeout=30,
)
```

## Events
You can subscribe to events using an initialized client, passing a lambda as a handeler:

```python
from firstclasspostcodes import Client

client = Client(api_key='wqrtythfgdvcs')

client.on('request', lambda **args : print(args))
```

| Event name | Description |
|:-----|:-----|
| `request` | Triggered before a request is sent. The request object to be sent is passed to the event handler. |
| `response` | Triggered with the parsed JSON response body upon a successful reques. |
| `error` | Triggered with a client error when the request fails. |
| `operation:{name}` | Triggered by an operation with the parameter object. |

**Note:** `{name}` is replaced with the operation name of the method, as defined inside the OpenAPI specification.

## Integration / Testing
We provide a mock service of our API as a docker container [available here](https://github.com/firstclasspostcodes/firstclasspostcodes-mock). Once the container is running, the library can be easily configured to use it:

```python
from firstclasspostcodes import Client
from urllib.parse import urlparse

MOCK_API_KEY = "111111111111"

uri = urlparse("http://localhost:3000")

client = Client(
    api_key=MOCK_API_KEY,
    protocol=uri.scheme,
    host=uri.netloc,
    base_path=uri.path,
)

client.get_postcode('AB30 1FR')
```