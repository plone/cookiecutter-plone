"""Pre Prompt hook."""
import sys

try:
    from cookieplone import data
    from cookieplone.utils import commands, console, sanity

    HAS_COOKIEPLONE = True
except ModuleNotFoundError:
    HAS_COOKIEPLONE = False


SUPPORTED_NODE_VERSIONS = [
    "18",
    "19",
    "20",
    "21",
    "22",
]


def _get_command_version(cmd: str) -> str:
    """Get version of a command."""
    try:
        raw_version = (
            subprocess.run([cmd, "--version"], capture_output=True)
            .stdout.decode()
            .strip()
        )
    except FileNotFoundError:
        raw_version = ""
    return raw_version


def check_node_version() -> str:
    """Check if Node version is supported."""
    raw_version = _get_command_version("node")
    major_version = raw_version[1:3] if raw_version else ""
    return (
        ""
        if major_version in SUPPORTED_NODE_VERSIONS
        else f"Node version is not supported: Got {raw_version}"
    )


def check_git_version() -> str:
    """Check if git is installed."""
    raw_version = _get_command_version("git")
    return "" if raw_version else "Git not found."


def sanity_check() -> data.SanityCheckResults:
    """Run sanity checks on the system."""
    checks = [
        data.SanityCheck(
            "Node",
            commands.check_node_version,
            [SUPPORTED_NODE_VERSIONS],
            "error",
        ),
        data.SanityCheck("git", commands.check_command_is_available, ["git"], "error"),
    ]
    result = sanity.run_sanity_checks(checks)
    return result

def main():
    """Validate context."""
    if not HAS_COOKIEPLONE:
        print("This template should be run with cookieplone")
        sys.exit(1)

    check_results = sanity_check()
    msg = "Creating a new Volto Addon"
    for check in check_results.checks:
        label = "green" if check.status else "red"
        msg = f"{msg}\n  - {check.name}: [{label}]{check.message}[/{label}]"
    console.panel(
        title="Volto Addon",
        msg=msg
    )
    if not check_results.status:
        sys.exit(1)

if __name__ == "__main__":
    main()
