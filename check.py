import unittest
import pkg_resources
import hashlib


class TestRequirements(unittest.TestCase):

    def test_requirements(self):
        """Test that each required package is available."""
        with open("requirements.txt") as f:
            lines = f.readlines()
        requirements = pkg_resources.parse_requirements(lines)
        for requirement in requirements:
            requirement = str(requirement)
            with self.subTest(requirement=requirement):
                pkg_resources.require(requirement)

    def test_data(self):
        """Test that the data is there"""
        with open("data/sha512.checksums") as f:
            lines = f.readlines()
        for pair in lines:
            orig_sha512, _file = pair.strip().split()
            sha512 = hashlib.sha512()
            with open("data/" + _file, 'rb') as f:
                while True:
                    data = f.read(65536)
                    if not data:
                        break
                    sha512.update(data)
            self.assertEqual(orig_sha512, sha512.hexdigest())
           


if __name__ == '__main__':

    unittest.main()
