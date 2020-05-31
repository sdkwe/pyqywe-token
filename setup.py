# -*- coding: utf-8 -*-

from setuptools import setup


version = '1.0.0'


setup(
    name='pyqywe-token',
    version=version,
    keywords='Wechat Weixin Access Token',
    description='Wechat Access Token Module for Python.',
    long_description=open('README.rst').read(),

    url='https://github.com/sdkwe/pyqywe-token',

    author='Hackathon',
    author_email='kimi.huang@brightcells.com',

    packages=['pyqywe_token'],
    py_modules=[],
    install_requires=['pywe_base', 'pywe_exception', 'pywe_storage'],

    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
