# -*- encoding: utf-8 -*-

from setuptools import setup
from setuptools import find_packages

setup(
    name="django-contact-plus",
    version="0.0.1",
    author_email="admin@arteria.ch",
    packages=find_packages(),
    include_package_data=True,
    description='Core of cmsplugin_contact_plus extracted as a standalone Django app',
)
