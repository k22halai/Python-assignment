#!/usr/bin/env python3
"""
Uploads all 12 sessions under the parent repository 'fundamental-of-python-language'
to GitHub under account k22halai.
"""

import os
import sys
import json
import urllib.request
import urllib.error
import subprocess

REPO_NAME = "fundamental-of-python-language"
REPO_DESC = "Fundamentals of Python Language - Complete Course Sessions 1 through 12"

def get_credentials():
    res = subprocess.run(
        ['git', 'credential', 'fill'],
        input='protocol=https\nhost=github.com\n',
        capture_output=True, text=True
    )
    cred = dict(l.split('=', 1) for l in res.stdout.splitlines() if '=' in l)
    return cred.get('username'), cred.get('password')

def try_create_repo(token):
    url = "https://api.github.com/user/repos"
    payload = json.dumps({
        "name": REPO_NAME,
        "description": REPO_DESC,
        "private": False,
        "auto_init": False
    }).encode()
    req = urllib.request.Request(
        url, data=payload,
        headers={"Authorization": f"token {token}", "User-Agent": "ParentUploader", "Content-Type": "application/json"},
        method="POST"
    )
    try:
        with urllib.request.urlopen(req) as resp:
            return True, "Created"
    except urllib.error.HTTPError as e:
        if e.code == 422:
            return True, "Already exists"
        return False, e.read().decode()

def push(username, token):
    auth_url = f"https://{username}:{token}@github.com/{username}/{REPO_NAME}.git"
    clean_url = f"https://github.com/{username}/{REPO_NAME}.git"

    subprocess.run(f'git remote set-url origin "{auth_url}"', shell=True)
    res = subprocess.run("git push -u origin main --force", shell=True, capture_output=True, text=True)
    subprocess.run(f'git remote set-url origin "{clean_url}"', shell=True)

    if res.returncode == 0:
        return True, f"https://github.com/{username}/{REPO_NAME}"
    else:
        return False, res.stderr.strip() or res.stdout.strip()

def main():
    print("=" * 65)
    print("   UPLOAD FUNDAMENTALS OF PYTHON LANGUAGE (ALL 12 SESSIONS)")
    print("=" * 65)

    username, token = get_credentials()
    if not username or not token:
        print("[-] Could not retrieve GitHub credentials.")
        sys.exit(1)

    print(f"[+] GitHub Account: {username}")
    print(f"[+] Repository: {REPO_NAME}")

    created, msg = try_create_repo(token)
    if not created:
        print("\n[!] Notice: GitHub API creation limit is active on token.")
        print(f"    Please click this 1-click link to create the empty repo in your browser:")
        print(f"    👉 https://github.com/new?name={REPO_NAME}&public=true\n")
        print("    (Click 'Create repository', leave everything unchecked)")
        input("    Press [Enter] after creating it to push immediately...")

    print("\n[+] Pushing all 12 sessions to GitHub...")
    success, result = push(username, token)
    if success:
        print(f"\n[SUCCESS] All 12 sessions are live at:\n👉 {result}")
    else:
        print(f"\n[-] Push failed: {result}")

if __name__ == "__main__":
    main()
