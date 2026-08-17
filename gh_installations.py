#!/usr/bin/env python3
"""List the GitHub App installations on your account and what they can reach.

This mirrors https://github.com/settings/installations from the command line.
Authenticate with a personal access token exported as GITHUB_TOKEN (or passed
with --token); no third-party packages are required.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request

API_ROOT = "https://api.github.com"
USER_AGENT = "gh-installations"


class GitHubError(RuntimeError):
    """An API call came back with a non-success status."""


def parse_next_link(link_header):
    """Return the URL marked rel="next" in a Link header, or None."""
    if not link_header:
        return None
    for part in link_header.split(","):
        segments = part.split(";")
        if len(segments) < 2:
            continue
        url = segments[0].strip()
        if not (url.startswith("<") and url.endswith(">")):
            continue
        for attribute in segments[1:]:
            key, _, value = attribute.strip().partition("=")
            if key.strip() == "rel" and value.strip().strip('"') == "next":
                return url[1:-1]
    return None


def _request(url, token):
    request = urllib.request.Request(
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "User-Agent": USER_AGENT,
            "X-GitHub-Api-Version": "2022-11-28",
        },
    )
    try:
        with urllib.request.urlopen(request) as response:
            payload = json.load(response)
            return payload, parse_next_link(response.headers.get("Link"))
    except urllib.error.HTTPError as error:
        detail = error.read().decode("utf-8", "replace").strip()
        raise GitHubError(f"{error.code} {error.reason} for {url}: {detail}") from error
    except urllib.error.URLError as error:
        raise GitHubError(f"could not reach {url}: {error.reason}") from error


def paginate(url, token, key):
    """Yield every item under `key` across all pages starting at `url`."""
    while url:
        payload, url = _request(url, token)
        yield from payload.get(key, [])


def list_installations(token):
    return list(paginate(f"{API_ROOT}/user/installations", token, "installations"))


def list_installation_repositories(token, installation_id):
    url = f"{API_ROOT}/user/installations/{installation_id}/repositories"
    return list(paginate(url, token, "repositories"))


def summarize_installation(installation):
    """Reduce an installation payload to the fields we actually print."""
    account = installation.get("account") or {}
    return {
        "id": installation.get("id"),
        "app": installation.get("app_slug") or "unknown-app",
        "account": account.get("login") or "unknown-account",
        "account_type": account.get("type") or "Unknown",
        "repository_selection": installation.get("repository_selection") or "unknown",
    }


def format_installation(summary, repositories=None):
    """Render one installation as the two-or-more lines shown to the user."""
    lines = [
        f"#{summary['id']}  {summary['app']}"
        f"  (account: {summary['account']}, {summary['account_type']})",
        f"    repository access: {summary['repository_selection']}",
    ]
    if repositories is not None:
        if repositories:
            lines.extend(f"      - {name}" for name in repositories)
        else:
            lines.append("      (no repositories)")
    return "\n".join(lines)


def resolve_token(explicit_token):
    token = explicit_token or os.environ.get("GITHUB_TOKEN")
    if not token:
        raise GitHubError(
            "no token found; export GITHUB_TOKEN or pass --token. "
            "A personal access token with the 'read:user' scope is enough."
        )
    return token


def build_report(token, include_repositories):
    report = []
    for installation in list_installations(token):
        summary = summarize_installation(installation)
        if include_repositories:
            repositories = [
                repository.get("full_name", "?")
                for repository in list_installation_repositories(token, summary["id"])
            ]
            summary["repositories"] = repositories
        report.append(summary)
    return report


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--token", help="GitHub token (defaults to $GITHUB_TOKEN)")
    parser.add_argument(
        "--repos",
        action="store_true",
        help="also list the repositories each installation can access",
    )
    parser.add_argument("--json", action="store_true", help="emit JSON instead of text")
    args = parser.parse_args(argv)

    try:
        token = resolve_token(args.token)
        report = build_report(token, args.repos)
    except GitHubError as error:
        print(f"error: {error}", file=sys.stderr)
        return 1

    if args.json:
        print(json.dumps(report, indent=2))
        return 0

    if not report:
        print("No GitHub App installations found for this account.")
        return 0

    print(f"{len(report)} installation(s)\n")
    for summary in report:
        print(format_installation(summary, summary.get("repositories")))
        print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
