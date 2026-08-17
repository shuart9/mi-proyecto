import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import gh_installations as gh


class ParseNextLinkTests(unittest.TestCase):
    def test_returns_next_url(self):
        header = (
            '<https://api.github.com/user/installations?page=2>; rel="next", '
            '<https://api.github.com/user/installations?page=5>; rel="last"'
        )
        self.assertEqual(
            gh.parse_next_link(header),
            "https://api.github.com/user/installations?page=2",
        )

    def test_returns_none_on_last_page(self):
        header = '<https://api.github.com/user/installations?page=1>; rel="prev"'
        self.assertIsNone(gh.parse_next_link(header))

    def test_returns_none_without_header(self):
        self.assertIsNone(gh.parse_next_link(None))
        self.assertIsNone(gh.parse_next_link(""))

    def test_ignores_malformed_segments(self):
        self.assertIsNone(gh.parse_next_link("garbage; rel=next-ish"))


class SummarizeInstallationTests(unittest.TestCase):
    def test_reads_the_fields_we_print(self):
        summary = gh.summarize_installation(
            {
                "id": 12345678,
                "app_slug": "claude",
                "repository_selection": "selected",
                "account": {"login": "shuart9", "type": "User"},
            }
        )
        self.assertEqual(
            summary,
            {
                "id": 12345678,
                "app": "claude",
                "account": "shuart9",
                "account_type": "User",
                "repository_selection": "selected",
            },
        )

    def test_falls_back_when_fields_are_missing(self):
        summary = gh.summarize_installation({"id": 1, "account": None})
        self.assertEqual(summary["app"], "unknown-app")
        self.assertEqual(summary["account"], "unknown-account")
        self.assertEqual(summary["account_type"], "Unknown")
        self.assertEqual(summary["repository_selection"], "unknown")


class FormatInstallationTests(unittest.TestCase):
    def setUp(self):
        self.summary = {
            "id": 42,
            "app": "claude",
            "account": "shuart9",
            "account_type": "User",
            "repository_selection": "selected",
        }

    def test_without_repositories(self):
        self.assertEqual(
            gh.format_installation(self.summary),
            "#42  claude  (account: shuart9, User)\n    repository access: selected",
        )

    def test_with_repositories(self):
        output = gh.format_installation(self.summary, ["shuart9/mi-proyecto"])
        self.assertIn("      - shuart9/mi-proyecto", output)

    def test_with_empty_repository_list(self):
        output = gh.format_installation(self.summary, [])
        self.assertIn("      (no repositories)", output)


class ResolveTokenTests(unittest.TestCase):
    def test_prefers_the_explicit_token(self):
        self.assertEqual(gh.resolve_token("explicit"), "explicit")

    def test_falls_back_to_the_environment(self):
        original = os.environ.get("GITHUB_TOKEN")
        os.environ["GITHUB_TOKEN"] = "from-env"
        try:
            self.assertEqual(gh.resolve_token(None), "from-env")
        finally:
            if original is None:
                del os.environ["GITHUB_TOKEN"]
            else:
                os.environ["GITHUB_TOKEN"] = original

    def test_raises_without_a_token(self):
        original = os.environ.pop("GITHUB_TOKEN", None)
        try:
            with self.assertRaises(gh.GitHubError):
                gh.resolve_token(None)
        finally:
            if original is not None:
                os.environ["GITHUB_TOKEN"] = original


class PaginateTests(unittest.TestCase):
    def test_follows_every_page(self):
        pages = {
            "page-1": ({"installations": [{"id": 1}]}, "page-2"),
            "page-2": ({"installations": [{"id": 2}]}, None),
        }
        calls = []

        def fake_request(url, token):
            calls.append(url)
            return pages[url]

        original = gh._request
        gh._request = fake_request
        try:
            items = list(gh.paginate("page-1", "token", "installations"))
        finally:
            gh._request = original

        self.assertEqual(items, [{"id": 1}, {"id": 2}])
        self.assertEqual(calls, ["page-1", "page-2"])


if __name__ == "__main__":
    unittest.main()
