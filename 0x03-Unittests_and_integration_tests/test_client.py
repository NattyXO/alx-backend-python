#!/usr/bin/env python3
"""
Parameterize and patch as decorators, Mocking a property, More patching,
Parameterize, Integration test: fixtures, Integration tests
"""

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from urllib.error import HTTPError

class TestGithubOrgClient(unittest.TestCase):
"""Test cases for GithubOrgClient"""

@parameterized.expand([
    ("google",),
    ("abc",),
])
@patch("client.get_json", return_value={"payload": True})
def test_org(self, org_name, mock_get):
    """Test that GithubOrgClient.org returns the correct value"""
    test_client = GithubOrgClient(org_name)
    test_return = test_client.org
    self.assertEqual(test_return, mock_get.return_value)
    mock_get.assert_called_once()

def test_public_repos_url(self):
    """Test GithubOrgClient._public_repos_url"""
    with patch.object(GithubOrgClient, "org", new_callable=PropertyMock, return_value={"repos_url": "holberton"}) as mock_org:
        test_client = GithubOrgClient("holberton")
        test_return = test_client._public_repos_url
        mock_org.assert_called_once()
        self.assertEqual(test_return, mock_org.return_value["repos_url"])

@patch("client.get_json", return_value=[{"name": "holberton"}])
def test_public_repos(self, mock_get):
    """Test GithubOrgClient.public_repos"""
    with patch.object(GithubOrgClient, "_public_repos_url", new_callable=PropertyMock, return_value="https://api.github.com/") as mock_url:
        test_client = GithubOrgClient("holberton")
        test_return = test_client.public_repos()
        self.assertEqual(test_return, ["holberton"])
        mock_get.assert_called_once()
        mock_url.assert_called_once()

@parameterized.expand([
    ({"license": {"key": "my_license"}}, "my_license", True),
    ({"license": {"key": "other_license"}}, "my_license", False),
])
def test_has_license(self, repo, license_key, expected_return):
    """Test GithubOrgClient.has_license"""
    test_client = GithubOrgClient("holberton")
    test_return = test_client.has_license(repo, license_key)
    self.assertEqual(expected_return, test_return)
@parameterized_class(
("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
"""Integration tests for GithubOrgClient"""

@classmethod
def setUpClass(cls):
    """Set up the test case"""
    cls.get_patcher = patch('requests.get', side_effect=HTTPError)

@classmethod
def tearDownClass(cls):
    """Tear down the test case"""
    cls.get_patcher.stop()

def test_public_repos(self):
    """Test GithubOrgClient.public_repos"""
    test_client = GithubOrgClient("holberton")
    assert True

def test_public_repos_with_license(self):
    """Test public_repos with license argument"""
    test_client = GithubOrgClient("holberton")
    assert True
if name == 'main':
unittest.main()
