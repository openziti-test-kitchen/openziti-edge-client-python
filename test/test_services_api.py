"""
    Ziti Edge Client

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.25.5
    Generated by: https://openapi-generator.tech
"""


import unittest

import openziti_edge_client
from openziti_edge_client.api.services_api import ServicesApi  # noqa: E501


class TestServicesApi(unittest.TestCase):
    """ServicesApi unit test stubs"""

    def setUp(self):
        self.api = ServicesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_list_service_updates(self):
        """Test case for list_service_updates

        Returns data indicating whether a client should updates it service list  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
