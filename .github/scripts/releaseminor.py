"""Stuff"""
import json
import subprocess


def get_last_version() -> str:
    """Return the version number of the last release."""
    json_string = (
        subprocess.run(
            ["gh", "release", "view", "--json", "tagName"],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        .stdout.decode("utf8")
        .strip()
    )

    return json.loads(json_string)["tagName"]


def bump_minor_number(version_number: str) -> str:
    """Return a copy of `version_number` with the minor number incremented."""
    major, minor, patch = version_number.split(".")
    patch = 0
    return f"{major}.{int(minor) + 1}.{patch}"


def create_new_minor_release():
    """Create a new minor release on GitHub."""
    try:
        last_version_number = get_last_version()
    except subprocess.CalledProcessError as err:
        if err.stderr.decode("utf8").startswith("HTTP 404:"):
            # The project doesn't have any releases yet.
            new_version_number = "0.1.0"
        else:
            raise
    else:
        new_version_number = bump_minor_number(last_version_number)

    subprocess.run(
        ["gh", "release", "create", "--generate-notes", new_version_number],
        check=True,
    )


if __name__ == "__main__":
    create_new_minor_release()
