"""
    Ziti Edge Client

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.25.5
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import openziti_edge_client
from openziti_edge_client.model.password import Password
from openziti_edge_client.model.tags import Tags
from openziti_edge_client.model.username import Username
globals()['Password'] = Password
globals()['Tags'] = Tags
globals()['Username'] = Username
from openziti_edge_client.model.authenticator_update import AuthenticatorUpdate


class TestAuthenticatorUpdate(unittest.TestCase):
    """AuthenticatorUpdate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAuthenticatorUpdate(self):
        """Test AuthenticatorUpdate"""
        # FIXME: construct object with mandatory attributes with example values
        # model = AuthenticatorUpdate()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
