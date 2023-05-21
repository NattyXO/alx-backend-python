#!/usr/bin/env python3
""" Unittest module """

from unittest import TestCase
from unittest.mock import patch, MagicMock
from parameterized import parameterized

import client
from client import GithubOrgClient

class TestGithubOrgClient(TestCase):
    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected_result):
        org_name = "example"
        with patch.object(GithubOrgClient, 'public_repos', return_value=[repo]):
            gc = GithubOrgClient(org_name)
            result = gc.has_license(license_key)
            self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
