# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

def read(*rnames):
    return open(
        os.path.join(
            os.path.join(os.path.dirname(__file__), 'docs'),
            *rnames)).read()

version = 0.1
long_description = read('README.txt') + '\n' + read('CHANGES.txt')

install_requires = [
    'cromlech.browser',
    'cromlech.io',
    'grokcore.component >= 2.1',
    'grokcore.security',
    'martian >= 0.13',
    'setuptools',
    'zope.component',
    'zope.location',
    ]

tests_require = [
    'cromlech.webob',
    'zope.configuration',
    'zope.interface',
    ]

security_require = [
    'grokcore.security >= 1.5',
    'zope.principalregistry',
    'zope.security',
    'zope.securitypolicy',
    ]

setup(
    name='dolmen.view',
    version=version,
    author='Grok & Dolmen Teams',
    author_email='',
    url='http://gitweb.dolmen-project.org',
    download_url='http://pypi.python.org/pypi/dolmen.view',
    description='Grok-like configuration for View components',
    long_description=long_description,
    license='ZPL',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Zope Public License',
        'Programming Language :: Python',
        ],
    packages=find_packages('src'),
    package_dir = {'': 'src'},
    namespace_packages=['dolmen'],
    include_package_data = True,
    zip_safe=False,
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={
        'test': tests_require,
        'security': security_require,
        },
)
