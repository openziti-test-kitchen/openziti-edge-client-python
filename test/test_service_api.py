"""
    Ziti Edge Client

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.25.5
    Generated by: https://openapi-generator.tech
"""


import unittest

import openziti_edge_client
from openziti_edge_client.api.service_api import ServiceApi  # noqa: E501


class TestServiceApi(unittest.TestCase):
    """ServiceApi unit test stubs"""

    def setUp(self):
        self.api = ServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_service(self):
        """Test case for delete_service

        Delete a service  # noqa: E501
        """
        pass

    def test_detail_service(self):
        """Test case for detail_service

        Retrieves a single service  # noqa: E501
        """
        pass

    def test_list_service_terminators(self):
        """Test case for list_service_terminators

        List of terminators assigned to a service  # noqa: E501
        """
        pass

    def test_list_services(self):
        """Test case for list_services

        List services  # noqa: E501
        """
        pass

    def test_patch_service(self):
        """Test case for patch_service

        Update the supplied fields on a service  # noqa: E501
        """
        pass

    def test_update_service(self):
        """Test case for update_service

        Update all fields on a service  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
