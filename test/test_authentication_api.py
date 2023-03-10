"""
    Ziti Edge Client

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.25.5
    Generated by: https://openapi-generator.tech
"""


import unittest

import openziti_edge_client
from openziti_edge_client.api.authentication_api import AuthenticationApi  # noqa: E501


class TestAuthenticationApi(unittest.TestCase):
    """AuthenticationApi unit test stubs"""

    def setUp(self):
        self.api = AuthenticationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_authenticate(self):
        """Test case for authenticate

        Authenticate via a method supplied via a query string parameter  # noqa: E501
        """
        pass

    def test_authenticate_mfa(self):
        """Test case for authenticate_mfa

        Complete MFA authentication  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
