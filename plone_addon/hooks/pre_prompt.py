"""Pre Prompt hook."""
import subprocess
import sys

try:
    from cookieplone import data
    from cookieplone import utils
    HAS_COOKIEPLONE = True
except ModuleNotFoundError:
    HAS_COOKIEPLONE = False


SUPPORTED_PYTHON_VERSIONS = [
    "3.8",
    "3.9",
    "3.10",
    "3.11",
    "3.12",
]


def sanity_check() -> bool:
    """Run sanity checks on the system."""
    checks = [
        data.SanityCheck("Python", utils.commands.check_python_version, [SUPPORTED_PYTHON_VERSIONS], "error"),
        data.SanityCheck("git", utils.commands.check_command_is_available, ["git"], "error"),
    ]
    result = utils.sanity.run_sanity_checks(checks)
    return result.status


def main():
    """Validate context."""
    if not HAS_COOKIEPLONE:
        print("This template should be run with cookieplone")
        sys.exit(1)
    utils.console.panel(
        title="Plone Addon",
        msg="Creating a new Plone Addon"
    )
    if not sanity_check():
        sys.exit(1)


if __name__ == "__main__":
    main()
