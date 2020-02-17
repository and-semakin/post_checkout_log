#!/usr/bin/env python3
import csv
import subprocess
import sys
import os
from pathlib import Path
from datetime import datetime

log_file = Path("~/.git_history").expanduser()
log_file.touch(mode=0o644, exist_ok=True)


def git(command: str, repo: os.PathLike) -> str:
    output = subprocess.check_output(
        f"git {command}", shell=True, cwd=repo
    ).decode()
    return output


def log(repo: os.PathLike, prev_head: str, next_head: str) -> None:
    print(f"Checkout logged: {prev_head} -> {next_head}")
    time = datetime.utcnow().isoformat()
    with log_file.open("a") as f:
        writer = csv.writer(f)
        writer.writerow([time, str(repo), prev_head, next_head])


repo = Path(os.getcwd())
previous_head: str = sys.argv[1]
next_head: str = sys.argv[2]
branch_checkout: bool = sys.argv[3] == "1"

if branch_checkout:
    previous_branch = git(
        f"name-rev --refs=\"refs/heads/*\" --always --name-only {previous_head}",
        repo
    ).strip()
    next_branch = git(
        f"name-rev --refs=\"refs/heads/*\" --always --name-only {next_head}",
        repo
    ).strip()
    log(repo, previous_branch, next_branch)
else:
    log(repo, previous_head, next_head)
