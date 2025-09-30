import unittest
from github_repos567 import get_user_repos_and_commits

class TestGitHubAPI(unittest.TestCase):

    def test_valid_user(self):
        """Test with a known GitHub user who has public repos"""
        results = get_user_repos_and_commits("swin0")
        self.assertIsInstance(results, list)
        self.assertGreater(len(results), 0)  

    def test_nonexistent_user(self):
        """Test with a user that does not exist"""
        results = get_user_repos_and_commits("thisuserdoesnotexist123456789")
        self.assertEqual(results, []) 

    def test_empty_user(self):
        """Test with empty string"""
        results = get_user_repos_and_commits("")
        self.assertEqual(results, []) 

if __name__ == "__main__":
    unittest.main()
