"""
    Ziti Edge Client

    OpenZiti Edge Client API  # noqa: E501

    The version of the OpenAPI document: 0.25.5
    Contact: help@openziti.org
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "openziti-edge-client"
VERSION = "0.24.87"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
  "urllib3 >= 1.25.3",
  "python-dateutil",
]

setup(
    name=NAME,
    version=VERSION,
    description="Ziti Edge Client",
    author="OpenZiti",
    author_email="help@openziti.org",
    url="https://github.com/openziti-test-kitchen/openziti-edge-client-python",
    keywords=["OpenAPI", "OpenAPI-Generator", "Ziti Edge Client"],
    python_requires=">=3.6",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="Apache 2.0",
    long_description="""\
    OpenZiti Edge Client API  # noqa: E501
    """
)
