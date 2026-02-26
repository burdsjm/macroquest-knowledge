#!/usr/bin/env python3
"""
Fetch MacroQuest documentation from the macroquest/docs GitHub repository
and save it as markdown files organized for use as an AI knowledge base.

Files are downloaded from raw.githubusercontent.com and saved preserving
the original directory structure from the source repository.

Usage:
    python3 scripts/fetch_docs.py [--output-dir DIR] [--delay SECONDS]
"""

import argparse
import json
import os
import re
import sys
import time
from pathlib import Path
import urllib.request
import urllib.error


REPO_OWNER = "macroquest"
REPO_NAME = "docs"
BRANCH = "master"
RAW_BASE = f"https://raw.githubusercontent.com/{REPO_OWNER}/{REPO_NAME}/{BRANCH}"

# Directories to mirror from the source repo (all .md files under these dirs)
MIRROR_DIRS = [
    "reference",
    "macros",
    "lua",
    "plugins",
    "main",
    "ai_helpers",
]

# Top-level markdown files to include
MIRROR_FILES = [
    "README.md",
]


def fetch_raw(path: str) -> str:
    """Download a raw file from the repository and return its contents."""
    url = f"{RAW_BASE}/{path}"
    req = urllib.request.Request(url)
    req.add_header("User-Agent", "macroquest-knowledge-fetcher")
    with urllib.request.urlopen(req) as response:
        return response.read().decode("utf-8", errors="replace")


def get_file_list() -> list[str]:
    """
    Parse mkdocs.yml to collect the list of all .md files referenced in the
    documentation. Also discovers files via the GitHub Contents API for
    directories that use glob patterns (e.g. ai_helpers/*).
    """
    print("Fetching mkdocs.yml to enumerate documentation files...")
    mkdocs = fetch_raw("mkdocs.yml")

    # Extract all .md file paths referenced in mkdocs.yml
    paths = set(re.findall(r"[\w./-]+\.md", mkdocs))

    # Keep only paths that are in our target directories or are top-level files
    def _want(p: str) -> bool:
        if "/" not in p and p in MIRROR_FILES:
            return True
        return any(p.startswith(d + "/") for d in MIRROR_DIRS)

    collected = set(p for p in paths if _want(p))

    # Discover files from directories that may use glob patterns in mkdocs.yml
    # (e.g. "ai_helpers/*") by fetching the directory listing from GitHub.
    _discover_dir_files(collected)

    return sorted(collected)


def _discover_dir_files(paths: set, branch: str = BRANCH):
    """
    For each directory in MIRROR_DIRS that has fewer than expected .md files,
    fetch its listing from the GitHub Contents API and add discovered .md paths.
    This catches files not individually listed in mkdocs.yml navigation.
    """
    # Use the GitHub Contents API (no auth needed for public repos, 60 req/hr)
    api_base = "https://api.github.com"

    def _list_dir(repo_path: str):
        url = f"{api_base}/repos/{REPO_OWNER}/{REPO_NAME}/contents/{repo_path}?ref={branch}"
        req = urllib.request.Request(url)
        req.add_header("User-Agent", "macroquest-knowledge-fetcher")
        req.add_header("Accept", "application/vnd.github.v3+json")
        try:
            with urllib.request.urlopen(req) as resp:
                return json.loads(resp.read().decode())
        except Exception:
            return []

    for d in MIRROR_DIRS:
        items = _list_dir(d)
        for item in items:
            if item.get("type") == "file" and item["path"].endswith(".md"):
                paths.add(item["path"])
            elif item.get("type") == "dir":
                # One level of recursion for subdirectories
                sub_items = _list_dir(item["path"])
                for sub in sub_items:
                    if sub.get("type") == "file" and sub["path"].endswith(".md"):
                        paths.add(sub["path"])


def fetch_all(output_dir: Path, delay: float = 0.1):
    """Download all documentation files to the output directory."""
    paths = get_file_list()
    print(f"Found {len(paths)} documentation files to download.\n")

    errors = []
    for i, path in enumerate(paths, 1):
        dest = output_dir / path
        dest.parent.mkdir(parents=True, exist_ok=True)

        print(f"[{i:3}/{len(paths)}] {path}")
        try:
            content = fetch_raw(path)
            dest.write_text(content, encoding="utf-8")
        except Exception as e:
            print(f"         ERROR: {e}", file=sys.stderr)
            errors.append((path, str(e)))

        if delay > 0:
            time.sleep(delay)

    print(f"\nDone. {len(paths) - len(errors)} files written to {output_dir}")
    if errors:
        print(f"{len(errors)} files failed:", file=sys.stderr)
        for path, err in errors:
            print(f"  {path}: {err}", file=sys.stderr)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-dir",
        default=str(Path(__file__).resolve().parent.parent / "docs"),
        help="Directory to write documentation files (default: docs/ next to this script)",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=0.1,
        help="Seconds to wait between requests (default: 0.1)",
    )
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    fetch_all(output_dir, delay=args.delay)


if __name__ == "__main__":
    main()
