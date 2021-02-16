# coding: utf-8

"""
    Kanbanflow API

    Lean project management. Simplified.  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "pykanbanflow"
VERSION = "0.1"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Kanbanflow API",
    author_email="",
    url="https://github.com/riccardomc/pykanbanflow",
    keywords=["Swagger", "Kanbanflow API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    Lean project management. Simplified.  # noqa: E501
    """
)
