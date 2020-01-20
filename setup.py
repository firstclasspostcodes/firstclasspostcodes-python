import os
from codecs import open
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

os.chdir(here)

version_contents = {}
with open(os.path.join(here, "firstclasspostcodes", "version.py"), encoding="utf-8") as f:
    exec(f.read(), version_contents)

setup(
    name='firstclasspostcodes',
    version=version_contents["VERSION"],
    url='https://github.com/firstclasspostcodes/firstclasspostcodes-python',
    license='MIT',
    keywords="firstclasspostcodes postcode uk api",
    author='Firstclasspostcodes',
    author_email='support@firstclasspostcodes.com',
    description="Python bindings for the Firstclasspostcodes API",
    packages=find_packages(exclude=['tests', 'tests.*']),
    long_description=open('README.md').read(),
    install_requires=[
        'requests >= 2.20; python_version >= "3.0"',
        'requests[security] >= 2.20; python_version < "3.0"',
    ],
    project_urls={
        "Bug Tracker": "https://github.com/firstclasspostcodes/firstclasspostcodes-python/issues",
        "Documentation": "https://github.com/firstclasspostcodes/firstclasspostcodes-python",
        "Source Code": "https://github.com/firstclasspostcodes/firstclasspostcodes-python",
    },
    zip_safe=False
)
