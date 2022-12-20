"""
    Ziti Edge Client

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.25.5
    Generated by: https://openapi-generator.tech
"""


import unittest

import openziti_edge_client
from openziti_edge_client.api.extend_enrollment_api import ExtendEnrollmentApi  # noqa: E501


class TestExtendEnrollmentApi(unittest.TestCase):
    """ExtendEnrollmentApi unit test stubs"""

    def setUp(self):
        self.api = ExtendEnrollmentApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_extend_current_identity_authenticator(self):
        """Test case for extend_current_identity_authenticator

        Allows the current identity to recieve a new certificate associated with a certificate based authenticator  # noqa: E501
        """
        pass

    def test_extend_router_enrollment(self):
        """Test case for extend_router_enrollment

        Extend the life of a currently enrolled router's certificates  # noqa: E501
        """
        pass

    def test_extend_verify_current_identity_authenticator(self):
        """Test case for extend_verify_current_identity_authenticator

        Allows the current identity to validate reciept of a new client certificate  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()