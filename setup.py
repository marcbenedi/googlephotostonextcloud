#!/usr/bin/env python

import os
import sys
import re

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()


def read_init_file():
    content = open('googlephotostonextcloud/__init__.py', 'r').read()

    version = re.search(r'__version__ = "(.*?)"', content)
    author_email = re.search(r'__email__ = "(.*?)"', content)
    author_name = re.search(r'__author__ = "(.*?)"', content)

    version = version.group(1) if version else 'Not found'
    author_email = author_email.group(1) if author_email else 'Not found'
    author_name = author_name.group(1) if author_name else 'Not found'

    return version, author_email, author_name

version, author_email, author_name = read_init_file()

readme = open('README.md').read()
doclink = """
Documentation
-------------

The full documentation is at http://googlephotostonextcloud.rtfd.org."""
history = open('HISTORY.md').read()

setup(
    name='googlephotostonextcloud',
    version=version,
    description='Python tool to migrate Google Photos Takout to NextCloud',
    long_description=readme + '\n\n' + doclink + '\n\n' + history,
    author=author_name,
    author_email=author_email,
    url='https://github.com/marcbenedi/googlephotostonextcloud',
    packages=[
        'googlephotostonextcloud',
    ],
    package_dir={'googlephotostonextcloud': 'googlephotostonextcloud'},
    include_package_data=True,
    install_requires=[
    ],
    license='MIT',
    zip_safe=False,
    keywords='googlephotostonextcloud',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
)
