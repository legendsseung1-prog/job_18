import importlib
import unittest
from unittest.mock import patch


class SearchUrlTests(unittest.TestCase):
    def test_build_search_url_includes_keyword_and_first_page(self):
        with patch("requests.get"):
            scrapper = importlib.import_module("scrapper")

        self.assertEqual(
            scrapper.build_search_url("파이썬"),
            "https://search.incruit.com/list/search.asp?col=job&kw=파이썬&startno=0",
        )


if __name__ == "__main__":
    unittest.main()
