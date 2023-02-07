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


def bump_major_number(version_number: str) -> str:
    """Return a copy of `version_number` with the major number incremented."""
    major, minor, patch = version_number.split(".")
    minor = 0
    patch = 0
    return f"{int(major) + 1}.{minor}.{patch}"


def create_new_major_release():
    """Create a new major release on GitHub."""
    try:
        last_version_number = get_last_version()
    except subprocess.CalledProcessError as err:
        if err.stderr.decode("utf8").startswith("HTTP 404:"):
            # The project doesn't have any releases yet.
            new_version_number = "1.0.0"
        else:
            raise
    else:
        new_version_number = bump_major_number(last_version_number)

    subprocess.run(
        ["gh", "release", "create", "--generate-notes", new_version_number],
        check=True,
    )


if __name__ == "__main__":
    create_new_major_release()
