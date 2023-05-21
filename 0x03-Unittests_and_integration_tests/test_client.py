#!/usr/bin/env python3
""" Unittest module """

from unittest import TestCase, mock
from unittest.mock import patch

import client
from client import GithubOrgClient

class TestGithubOrgClient(TestCase):
    def test_public_repos_url(self):
        org_name = "example"
        payload = {"url": "https://api.github.com/orgs/example"}

        with patch.object(GithubOrgClient, 'org', new_callable=mock.PropertyMock) as mock_org:
            mock_org.return_value = payload

            gc = GithubOrgClient(org_name)
            result = gc._public_repos_url

            expected_url = payload["url"]
            self.assertEqual(result, expected_url)

if __name__ == '__main__':
    unittest.main()
