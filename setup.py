# coding: utf-8
import os.path
import io
import re

from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))
# README = io.open(os.path.join(here, 'README.rst'), encoding='utf8').read()
# CHANGES = io.open(os.path.join(here, 'CHANGES.txt'), encoding='utf8').read()

with io.open(os.path.join(here, 'giles', '__init__.py'),
             encoding='utf8') as version_file:
    metadata = dict(re.findall(r"""__([a-z]+)__ = "([^"]+)""",
                               version_file.read()))

setup(
    name='giles-athenaeum',
    version=metadata['version'],
    description='A REST API library catalog',
    # long_description=README + '\n\n' + CHANGES,
    classifiers=[
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3 :: Only"
    ],
    author='Mason Egger',
    author_email='mason@masonegger.com',
    url='https://www.masonegger.com',
    keywords=['library', 'ils', 'REST'],
    license='BSD-2',
    packages=find_packages(),
    python_requires=">=3.4",
    include_package_data=True,
    zip_safe=False,
)
