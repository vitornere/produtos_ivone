# -*- coding: utf8 -*-
#
# This file were created by Python Boilerplate. Use boilerplate to start simple
# usable and best-practices compliant Python projects.
#
# Learn more about it at: http://github.com/fabiommendes/boilerplate/
#

import os
from setuptools import setup, find_packages


# Meta information
version = open('VERSION').read().strip()
dirname = os.path.dirname(__file__)


# Save version and author to __meta__.py
base = os.path.join(dirname, 'src')
data = '''# Automatically created. Please do not edit.
__version__ = u'%s'
__author__ = u'F\\xe1bio Mac\\xeado Mendes'
''' % version
if os.path.exists(base):
    path = os.path.join(base, '__meta__.py')
    with open(path, 'wb') as F:
        F.write(data.encode())

# Obtain long description from README.rst
if os.path.exists('README.rst'):
    long_description = open('README.rst').read()
else:
    long_description = ''


setup(
    # Basic info

    # Classifiers (see https://pypi.python.org/pypi?%3Aaction=list_classifiers)
    classifiers=[
    ],

    # Packages and depencies
    package_dir={'': 'src'},
    packages=find_packages('src'),
    install_requires=[
        'Django==1.9',
        'whitenoise>=2.0,<2.1'
        'gunicorn',
        'psycopg2',
    ],
    extras_require={
        'dev': [
            'invoke',
            'pytest>=3.0.7',
            'flake8',
            'tox',
            'pytest-cov',
            'pytest-django>=2.9.1',
            'pytest-selenium',
            'pytest-factoryboy',
            'sulfur>=0.1.3',
            'docker-composer',
        ]
    },

    # Other configurations
    zip_safe=False,
    platforms='any',
)
