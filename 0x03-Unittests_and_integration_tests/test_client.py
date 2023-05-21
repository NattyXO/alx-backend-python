#!/usr/bin/env python3
""" Unittest module """

import unittest
from unittest.mock import patch
from parameterized import parameterized_class

import client
from client import GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


class TestGithubOrgClient(unittest.TestCase):
    def test_public_repos_url(self):
        org_name = "example"
        payload = {"url": "https://api.github.com/orgs/example"}

        with patch.object(GithubOrgClient, 'org', new_callable=unittest.mock.PropertyMock) as mock_org:
            mock_org.return_value = payload

            gc = GithubOrgClient(org_name)
            result = gc._public_repos_url

            expected_url = payload["url"]
            self.assertEqual(result, expected_url)

    @patch('client.get_json', return_value=repos_payload)
    @patch.object(GithubOrgClient, '_public_repos_url', new_callable=unittest.mock.PropertyMock)
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        gc = GithubOrgClient("example")
        repos = gc.public_repos()

        mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once()

        self.assertEqual(repos, expected_repos)

    @parameterized_class("org_payload", "repos_payload", "expected_repos", "apache2_repos")
    class TestIntegrationGithubOrgClient(unittest.TestCase):
        @classmethod
        def setUpClass(cls):
            cls.get_patcher = patch('requests.get')
            cls.mock_get = cls.get_patcher.start()

            cls.mock_get.side_effect = lambda url: MagicMock(json=lambda: cls.org_payload if url.endswith("/example") else cls.repos_payload)

        @classmethod
        def tearDownClass(cls):
            cls.get_patcher.stop()

        def test_public_repos(self):
            gc = GithubOrgClient("example")
            repos = gc.public_repos()
            self.assertEqual(repos, self.expected_repos)

        def test_public_repos_with_license(self):
            gc = GithubOrgClient("example")
            repos = gc.public_repos(license="apache-2.0")
            self.assertEqual(repos, self.apache2_repos)


if __name__ == '__main__':
    unittest.main()
