#!/usr/bin/env python
# -*- coding: utf8 -*-

"""setup
(C) Franck Barbenoire <fbarbenoire@yahoo.fr>
License : GPL v3"""

from distutils.core import setup
from setuptools import find_packages

setup(name = "django-saladoplayer",
    version = "0.2.4",
    description = "Django application for displaying spherical panoramas using SaladoPlayer flash viewer",
    author = "Franck Barbenoire",
    author_email = "fbarbenoire@yahoo.fr",
    url = "https://github.com/franckinux/django-saladoplayer",
    packages = find_packages(),
    include_package_data = True,
    zip_safe = False,
    classifiers = ['Development Status :: 4 - Beta',
                   'License :: OSI Approved :: GNU General Public License (GPL)',
                   'Programming Language :: Python :: 2.6',
                   'Programming Language :: Python :: 2.7',
                   'Framework :: Django',
                   'Topic :: Internet :: WWW/HTTP :: Dynamic Content']
) 
