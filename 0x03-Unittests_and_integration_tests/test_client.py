#!/usr/bin/env python3
""" Unittest module """

from unittest import TestCase, mock
from unittest.mock import patch

import client
from client import GithubOrgClient

class TestGithubOrgClient(TestCase):
    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        org_name = "example"
        payload = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"}
        ]
        expected_repos = [repo["name"] for repo in payload]

        mock_get_json.return_value = payload

        with patch.object(GithubOrgClient, '_public_repos_url', new_callable=mock.PropertyMock) as mock_public_repos_url:
            gc = GithubOrgClient(org_name)
            repos = gc.public_repos()

            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once()

            self.assertEqual(repos, expected_repos)

if __name__ == '__main__':
    unittest.main()
