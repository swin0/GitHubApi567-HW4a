import unittest
from unittest.mock import patch, Mock
from github_repos567 import get_user_repos_and_commits

class TestGitHubAPI(unittest.TestCase):

    @patch("github_repos567.requests.get")
    def test_valid_user(self, mock_get):
        mock_repos = Mock()
        mock_repos.status_code = 200
        mock_repos.json.return_value = [{"name": "repo1"}, {"name": "repo2"}]

        mock_commits = Mock()
        mock_commits.status_code = 200
        mock_commits.json.return_value = [{}] * 5  
        mock_get.side_effect = [mock_repos, mock_commits, mock_commits]

        results = get_user_repos_and_commits("fakeuser")
        self.assertEqual(results, [("repo1", 5), ("repo2", 5)])

    @patch("github_repos567.requests.get")
    def test_nonexistent_user(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 404
        mock_response.json.return_value = []
        mock_get.return_value = mock_response

        results = get_user_repos_and_commits("fakeuser")
        self.assertEqual(results, [])

if __name__ == "__main__":
    unittest.main()
