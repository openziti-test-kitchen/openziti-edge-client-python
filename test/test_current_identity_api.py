"""
    Ziti Edge Client

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.25.5
    Generated by: https://openapi-generator.tech
"""


import unittest

import openziti_edge_client
from openziti_edge_client.api.current_identity_api import CurrentIdentityApi  # noqa: E501


class TestCurrentIdentityApi(unittest.TestCase):
    """CurrentIdentityApi unit test stubs"""

    def setUp(self):
        self.api = CurrentIdentityApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_mfa_recovery_codes(self):
        """Test case for create_mfa_recovery_codes

        For a completed MFA enrollment regenerate the recovery codes  # noqa: E501
        """
        pass

    def test_delete_mfa(self):
        """Test case for delete_mfa

        Disable MFA for the current identity  # noqa: E501
        """
        pass

    def test_detail_mfa(self):
        """Test case for detail_mfa

        Returns the current status of MFA enrollment  # noqa: E501
        """
        pass

    def test_detail_mfa_qr_code(self):
        """Test case for detail_mfa_qr_code

        Show a QR code for unverified MFA enrollments  # noqa: E501
        """
        pass

    def test_detail_mfa_recovery_codes(self):
        """Test case for detail_mfa_recovery_codes

        For a completed MFA enrollment view the current recovery codes  # noqa: E501
        """
        pass

    def test_enroll_mfa(self):
        """Test case for enroll_mfa

        Initiate MFA enrollment  # noqa: E501
        """
        pass

    def test_get_current_identity(self):
        """Test case for get_current_identity

        Return the current identity  # noqa: E501
        """
        pass

    def test_get_current_identity_edge_routers(self):
        """Test case for get_current_identity_edge_routers

        Return this list of Edge Routers the identity has access to  # noqa: E501
        """
        pass

    def test_verify_mfa(self):
        """Test case for verify_mfa

        Complete MFA enrollment by verifying a time based one time token  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
